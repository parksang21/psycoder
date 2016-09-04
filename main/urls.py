from django.conf.urls import url
from . import views


app_name = 'main'

urlpatterns = [



    # /history
    url(r'^history/$', views.history, name='history'),

    url(r'^register/$', views.register_view, name='signup'),

    url(r'^login/$', views.login_view, name='login'),

    url(r'^logout/$', views.logout_view, name='logout'),

#
    url(r'^$', views.IndexView.as_view(), name='index'),

]
