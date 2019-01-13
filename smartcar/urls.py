from django.conf.urls import include, url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^feedback/$', views.feedback, name='feedback'),
]