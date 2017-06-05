from django.http import HttpResponse
from django.template.loader import render_to_string


def index(request):
    rendered = render_to_string('hello_world.html')
    return HttpResponse(rendered)
