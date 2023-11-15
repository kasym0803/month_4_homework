from django.shortcuts import (HttpResponse)
from datetime import datetime

def Hello_view(request):
    return HttpResponse('Hello! Its my project')


def Date_view(request):
    current_date = datetime.now()
    format_date = current_date.strftime('%Y-%m-%d')
    return HttpResponse(f'Current Date {format_date}')


def Goodby_view(request):
    return HttpResponse('Goodbye user!')

