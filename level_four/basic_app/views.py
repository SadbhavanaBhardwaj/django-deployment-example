from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


def other(request):
    return render(request, 'basic_app/other.html')


def relative(request):
    return render(request, 'basic_app/relative_html_templates.html')
