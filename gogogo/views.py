# -*- coding: utf-8 -*-
from django.http import HttpResponse


def year_archive(request, year):
    return HttpResponse(year)
