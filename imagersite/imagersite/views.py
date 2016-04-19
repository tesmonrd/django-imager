from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from imager_profile.models import Profile
from imager_images.models import Photo, Album


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        pass


def photo_details(request, **kwargs):
    photo_id = kwargs.get('photo_id')
    user = User.objects.filter(id=kwargs.get('user_id')).first()
    image = user.photos.filter(id=photo_id).first()
    if image.published != 'public' or request.user_id != user.id:
        return HttpResponse("404")
    return render(request, 'photo_details.html', context={"image": image})


def library_view(request, *args, **kwargs):
    albums = request.user.albums.all()
    photos = request.user.photos.all()
    return render(request,
                  "library.html",
                  context={"albums": albums, "photos": photos})


def profile_details(request, profile_id=None, **kwargs):
    if not profile_id:
        profile = request.user.profile
    else:
        profile = get_object_or_404(Profile, id=int(profile_id))
    return render(request, "profile.html", context={"profile": profile})


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
