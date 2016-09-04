from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Album(models.Model):
    title = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('main:gallery', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Picture(models.Model):
    album = models.ForeignKey(Album)
    picture = models.FileField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.time)


class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email
