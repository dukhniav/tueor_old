# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def about(request):
    context = {'segment': 'about'}
    html_template = loader.get_template('core/about.html')
    return HttpResponse(html_template.render(context, request))


def contact(request):
    context = {'segment': 'contact'}
    html_template = loader.get_template('core/contact.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('core/index.html')
    return HttpResponse(html_template.render(context, request))
