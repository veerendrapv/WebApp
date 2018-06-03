from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login

#from django.contrib.generic import view  #can not import follow below one
from django.views import View
from django.http import HttpResponse,Http404
from django.template import loader
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Album3,Song3
from .forms import UserForm
from django.urls import reverse_lazy
def index(request):
    return HttpResponse("<h1>testing urls</h1>")
class IndexView(generic.ListView):
    template_name='videos/index.html'
    context_object_name='all_albums'
    #bydefault it will return with variable name of "object_list"
    def get_queryset(self):
        return Album3.objects.all()
class DetailView(generic.DetailView):
    model=Album3
    template_name='videos/detail.html'
class CreateAlbum(CreateView):
    model=Album3
    fields=['artist','album_title','genre','album_logo']
class AlbumUpdate(UpdateView):
    model=Album3
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album3
    success_url=reverse_lazy('videos:index')

class UserFormView(View):
    form_class=UserForm
    template_name='videos/registration_form.html'


    #to display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #process form data
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            #cleaned normalized data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #returns user objects if credentials are correct
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('videos:index')
        return render(request,self.template_name,{'form':form})

