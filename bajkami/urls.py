from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from bajkamiutkane.views import index, contact, offer, before, about, success, GalleryList, GalleryDetail

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', index, name='index'),
    url(r'^kontakt/$', contact, name='contact'),
    url(r'^oferta/$', offer, name='offer'),
    url(r'^przed_sesja/$', before, name='before'),
    url(r'^o_mnie/$', about, name='about'),
    url(r'^sukces/$', success, name='success'),
    url(r'^portfolio/$', GalleryList.as_view(), name='gallery-list'),
    url(r'^portfolio/(?P<slug>[\w\-_]+)/$', GalleryDetail.as_view(), name='gallery-detail'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
