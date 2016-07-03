# -*- coding: utf-8 -*-

import os
from cStringIO import StringIO

from django.db import models
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse

from PIL import Image as ImagePIL


class Gallery(models.Model):
    name = models.CharField('Nazwa galerii', max_length=50)
    slug = models.SlugField('Odnosnik', max_length=50, null=True, blank=True)
    date = models.DateTimeField('Data dodania', auto_now_add=True)
    cover = models.ImageField('Okładka', upload_to='static/galleries/covers/%Y/%m/%d')

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Galerie"
        ordering = ['date']

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('gallery', kwargs={'slug': self.slug})


class Image(models.Model):
    image = models.ImageField('Zdjęcie', upload_to='static/galleries/%Y/%m/%d')
    thumbnail = models.ImageField(upload_to='static/galleries/thumbnails/%Y/%m/%d', null=True, blank=True)
    gallery = models.ForeignKey(Gallery)
    date = models.DateTimeField('Data dodania', auto_now_add=True)
    description = models.CharField(max_length=160, verbose_name='Opis zdjęcia', null=True, blank=True)

    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"

    def __unicode__(self):
        return self.image.name

    def create_thumbnail(self):
        if not self.image:
            return

        THUMBNAIL_SIZE = (300, 250)
        DJANGO_TYPE = self.image.file.content_type

        if DJANGO_TYPE == 'image/jpeg':
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE == 'image/png':
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'
        image = ImagePIL.open(StringIO(self.image.read()))
        image.thumbnail(THUMBNAIL_SIZE, ImagePIL.ANTIALIAS)
        temp_handle = StringIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        suf = SimpleUploadedFile(os.path.split(self.image.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE)
        self.thumbnail.save('%s_thumbnail.%s' % (os.path.splitext(suf.name)[0], FILE_EXTENSION), suf, save=False)

    def save(self, *args, **kwargs):
        self.create_thumbnail()
        force_update = False
        if self.id:
            force_update = True
        super(Image, self).save(force_update=force_update)
