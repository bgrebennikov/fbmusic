from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.errMsg, name='errMsg'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
]
