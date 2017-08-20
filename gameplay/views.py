# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'gameplay/index.html')

def matchups(request):
    return render(request, 'gameplay/matchups.html')

def mechanics(request):
    return render(request, 'gameplay/mechanics.html')

def job_in_teamfights(request):
    return render(request, 'gameplay/job_in_teamfights.html')

def tricks(request):
    return render(request, 'gameplay/tricks.html')
