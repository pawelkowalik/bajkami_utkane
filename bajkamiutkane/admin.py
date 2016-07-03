# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bajkamiutkane.models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image',)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Image, ImageAdmin)
admin.site.register(Gallery, GalleryAdmin)