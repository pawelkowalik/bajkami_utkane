from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic

from bajkamiutkane.models import Gallery


def index(request):
    return render_to_response('index.html',
            {'': ''},
            context_instance=RequestContext(request))


def contact(request):
    return render_to_response('contact.html',
            {'': ''},
            context_instance=RequestContext(request))


def before(request):
    return render_to_response('before.html',
            {'': ''},
            context_instance=RequestContext(request))


def about(request):
    return render_to_response('about.html',
            {'': ''},
            context_instance=RequestContext(request))


def offer(request):
    return render_to_response('offer.html',
            {'': ''},
            context_instance=RequestContext(request))


class GalleryList(generic.ListView):
    model = Gallery
    context_object_name = 'gallery_list'
    queryset = Gallery.objects.order_by('date')


class GalleryDetail(generic.DetailView):
    model = Gallery
