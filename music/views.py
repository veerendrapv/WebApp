from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader
from .models import Albums,Songs
#def index(request):
#    return HttpResponse("<h1>testing urls</h1>")

def index11(request):
    all_albums=Albums.objects.all()
    html=''
    for album in all_albums:
        url='/music/'+str(album.id)+'/'
        html+="<a href="+url+">"+album.album_title+'</a><br>'
    return  HttpResponse(html)
def index2(request,album_id):
    albumobject=Albums.objects.get(pk=album_id)
    html="<h1>artist is"+albumobject.artist+"<br>title is "+albumobject.album_title+"</h1>"
    return HttpResponse(html)
    #return  HttpResponse("<h1>html</h1>")
# Create your views here.

def index3(request):
    all_albums = Albums.objects.all()
    template=loader.get_template('music/templatehtml.html')
    data="templatehtml"
    context={'album':data,'all_albums':all_albums}
    return HttpResponse(template.render(context,request))
def index4(request):
    all_albums = Albums.objects.all()
    #template=loader.get_template('music/templatehtml.html')
    data="render html"
    context={'album':data,'all_albums':all_albums}
    return render(request,'music/templatehtml.html',context)

def index5(request,album_id):
    try:
        album = Albums.objects.get(pk=album_id)
    except(Albums.DoesNotExist):
        return Http404("<h1>album with id not exist</h1>")
    #template=loader.get_template('music/templatehtml.html')
    context={'album':album}
    return render(request,'music/songtemplate.html',context)
def favorite(request,album_id):
    album=get_object_or_404(Albums,pk=album_id)
    try:
        selected_song=album.songs_set.get(pk=request.POST['song'])
    except(KeyError,Songs.DoesNotExist):
        return render(request,'music/detail.html',{'album':album,'error_message':'you did not select avalid song'})
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})

def index(request):
    context = {'album':'data'}
    return render(request, 'music/index.html', context)
def index22(request):
    all_albums = Albums.objects.all()
    context = {'albums':all_albums}
    return render(request, 'music/index2.html', context)