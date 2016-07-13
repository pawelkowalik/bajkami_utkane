# -*- coding: utf-8 -*-

from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_webpage = forms.CharField(required=False)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
