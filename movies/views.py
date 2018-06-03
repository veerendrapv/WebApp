from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album2,Song2
from django.urls import reverse_lazy
def index(request):
    return HttpResponse("<h1>testing urls</h1>")
class IndexView(generic.ListView):
    template_name='movies/index.html'
    context_object_name='all_albums'
    #bydefault it will return with variable name of "object_list"
    def get_queryset(self):
        return Album2.objects.all()
class DetailView(generic.DetailView):
    model=Album2
    template_name='movies/detail.html'
class CreateAlbum(CreateView):
    model=Album2
    fields=['artist','album_title','genre','album_logo']
class AlbumUpdate(UpdateView):
    model=Album2
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album2
    success_url=reverse_lazy('movies:index')