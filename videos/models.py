from django.db import models

# Create your models here.
from django.db import models
#from django.core.urlresolvers import reverse
from django.urls import reverse
class Album3(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=250)
    genre=models.CharField(max_length=100)
    album_logo=models.FileField()
    def get_absolute_url(self):
        return reverse('videos:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title+' - '+self.artist

class Song3(models.Model):
    album=models.ForeignKey(Album3,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title
    # Create your models here.
