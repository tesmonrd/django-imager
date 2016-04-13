from __future__ import unicode_literals
# from django.http import HttpResponse
# from django.shortcuts import render, render_to_response
# from django.template import loader
from django.views.generic import TemplateView


# def home_page(request, *args, **kwargs):
#     foo = 'garbanzo beans'
#     return render(request, 'home.html', context={'foo': foo})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        foo = 'garbanzo beans'
        return {'foo': foo}


class RegisView(TemplateView):
    template_name = ''
