from django.db import models


class DbTracks(models.Model):
    artist = models.CharField(max_length=64, blank=False, default='')
    trackName = models.CharField(max_length=120, blank=False, default='')
    description = models.TextField(blank=True, default='')
    img = models.ImageField()
    track_obj = models.FileField(upload_to="audio/", default="")
    date = models.DateTimeField()

    def __str__(self):
        if self.track_obj:
            return self.track_obj.url
    