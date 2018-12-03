from django.conf.urls import url, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url(r'^(?P<message_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^create_message/$', views.create_message,name='create_message'),
    url(r'^(?P<message_id>[0-9]+)/delete_message/$', views.delete_message, name='delete_message'),
    #url(r'^(?P<message_id>[0-9]+)/update_message/$', views.update_message, name='update_message'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^.*$', RedirectView.as_view(url='home', permanent=False), name='index')

    #url(r'^', include('home.urls', namespace='home')),
]


