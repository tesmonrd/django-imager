from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from imager_profile.models import Profile
from imager_images.models import Photo, Album
# from django.views.generic.details import DetailView
# from .imager_images.models import Photo


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


# class PhotoDetailView(DetailView):
#     model = Photo
#     template_name = "imager_images/photo_details.html"
class ProfileDetails(TemplateView):
    template_name = 'profile.html'
    model = Profile


class ImageDetails(TemplateView):
    template_name = 'image.html'
    model = Photo, Album


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
