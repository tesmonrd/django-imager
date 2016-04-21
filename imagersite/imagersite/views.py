from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from imager_profile.models import Profile
from django.forms import ModelForm
from imager_images.models import Photo, Album
from django.views.generic.edit import CreateView, UpdateView


class HomeView(TemplateView):
    template_name = 'home.html'


def photo_details(request, **kwargs):
    photo_id = kwargs.get('pk')
    user = User.objects.filter(id=kwargs.get('user_id')).first()
    image = user.photos.filter(id=photo_id).first()
    if image.published != 'public' or request.user.id != user.id:
        return HttpResponse("404")
    return render(request, 'photo_details.html', context={"image": image})


def library_view(request, *args, **kwargs):
    albums = request.user.albums.all()
    photos = request.user.photos.all()
    return render(request,
                  "library.html",
                  context={"albums": albums, "photos": photos})


def album_details(request, **kwargs):
    album_id = kwargs.get('pk')
    user = User.objects.filter(id=kwargs.get('user_id')).first()
    album = user.albums.filter(id=album_id).first()
    photos = user.albums.filter(id=album_id).first().photos.all()
    if request.user.id != user.id:
        return HttpResponse("404")
    return render(request, 'album_details.html',
                  context={'album': album, 'photos': photos})


def profile_details(request, profile_id=None, **kwargs):
    if not profile_id:
        profile = request.user.profile
    else:
        profile = get_object_or_404(Profile, id=int(profile_id))
    return render(request, "profile.html", context={"profile": profile})

# *********************** Add and Edit views ********************


class CreatePhoto(CreateView):
    """CreateView class for create photo."""

    model = Photo
    template_name = "photo_add.html"
    fields = ['image_file', 'image_title', 'image_description', 'published']

    def form_valid(self, form, *args, **kwargs):
        """Save information."""
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(CreatePhoto, self).form_valid(form)


class EditPhoto(UpdateView):
    """UpdateView for editing photo."""

    model = Photo
    template_name = "photo_edit.html"
    fields = ['image_title', 'image_description', 'published']

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(EditPhoto, self).form_valid(form)


class CreateAlbum(CreateView):
    """CreateView class for create album."""

    model = Album
    template_name = "album_add.html"
    fields = ['album_title',
              'album_description',
              'published',
              'photos',
              'cover']

    def get_form(self, form_class=None):
        form = super(CreateAlbum, self).get_form()
        form.fields['photos'].queryset = self.request.user.photos.all()
        return form

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(CreateAlbum, self).form_valid(form)


class EditAlbum(UpdateView):
    """UpdateView for editing album."""

    model = Album
    template_name = "album_edit.html"
    fields = ['album_title',
              'album_description',
              'published',
              'photos',
              'cover']

    def get_form(self, form_class=None):
        form = super(EditAlbum, self).get_form()
        form.fields['photos'].queryset = self.request.user.photos.all()
        return form

    def form_valid(self, form, *args, **kwargs):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user.id
        self.object.save()
        return super(EditAlbum, self).form_valid(form)


class EditUser(ModelForm):
    """Access User info."""

    class Meta:
        """Soooooo meta."""

        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class EditProfile(ModelForm):
    """Access Profile info."""

    class Meta:
        """Again soooo meta."""

        model = Profile
        fields = ['camera', 'location', 'picture_subject']


def edit_profile(request):
    current_user = User.objects.get(pk=request.user.id)
    current_profile = current_user.profile
    if request.method == 'POST':
        form1 = EditProfile(request.POST, instance=current_profile)
        form2 = EditUser(request.POST, instance=current_user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return render(request, 'profile.html')

    else:
        form1 = EditProfile(instance=current_profile)
        form2 = EditUser(instance=current_user)
    return render(request,
                  'profile_edit.html',
                  {'form1': form1, 'form2': form2})
