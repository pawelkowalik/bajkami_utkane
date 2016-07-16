# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.views import generic

from bajkamiutkane.models import Gallery
from bajkamiutkane.forms import ContactForm
from unidecode import unidecode


def index(request):
    return render_to_response('index.html',
            {'': ''},
            context_instance=RequestContext(request))


def contact(request):
    form_class = ContactForm(request.POST or None)

    if form_class.is_valid():
        contact_name = unidecode(form_class.cleaned_data['contact_name']),
        contact_email = unidecode(form_class.cleaned_data['contact_email']),
        contact_webpage = unidecode(form_class.cleaned_data['contact_webpage']),
        form_content = unidecode(form_class.cleaned_data['content']),

        # Email the profile with the
        # contact information
        template = get_template('contact_template.html')
        context = Context({
            'contact_name': contact_name,
            'contact_email': contact_email,
            'contact_webpage': contact_webpage,
            'form_content': form_content,
        })
        content = template.render(context)

        email = EmailMessage(
            "Nowy e-mail z bajkami-utkane.pl",
            content,
            contact_email,
            ["kontakt@bajkami-utkane.pl"],
            headers = {'Odpisz-do': contact_email }
        )
        email.content_subtype = "html"
        email.send()
        return redirect('about')
    else:
        return render(request, 'contact.html', {'form': form_class})


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
