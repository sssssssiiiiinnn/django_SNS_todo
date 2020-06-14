from django.http import HttpResponse
from django.views.generic import TemplateView


def hello_world_function(request):
    return HttpResponse('Hello world!!')


class HelloWorldView(TemplateView):
    template_name = 'hello.html'
