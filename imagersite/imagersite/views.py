from __future__ import unicode_literals
# from django.shortcuts import render, render_to_response
# from django.template import loader
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout


# def home_page(request, *args, **kwargs):
#     foo = 'garbanzo beans'
#     return render(request, 'home.html', context={'foo': foo})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        pass
        # try:
        #     img = Photo.objects.all().orger_by("?")[0]
        # except IndexError:
        #     img = None
        # return {'img': img}


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return("Account has been disabled :( ")
    else:
        return("Username or Password incorrect")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
