from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    category_title = models.CharField(max_length=500)
    category_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('main:course-list', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.category_title


class Course(models.Model):
    category = models.ForeignKey(Category)
    course_title = models.CharField(max_length=500)
    course_video = models.CharField(max_length=1000)
    course_add = models.DateTimeField(auto_now=True)
    course_text = models.TextField()

    def __str__(self):
        return self.course_title
