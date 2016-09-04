from django.conf.urls import url
from . import views

app_name = 'development'

urlpatterns = [

    # /development/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /development/<category>/
     url(r'^(?P<pk>[0-9]+)/$', views.CourseListView.as_view(), name='course-list'),


]