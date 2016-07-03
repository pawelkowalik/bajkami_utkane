from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from bajkamiutkane.views import index, contact, offer, GalleryList, GalleryDetail

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^offer/$', offer, name='offer'),
    url(r'^galleries/$', GalleryList.as_view(), name='gallery-list'),
    url(r'^gallery/(?P<slug>[\w\-_]+)/$', GalleryDetail.as_view(), name='gallery-detail'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
