# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Vision/base.html', name='index')
