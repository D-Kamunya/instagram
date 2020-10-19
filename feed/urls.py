from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.home_page,name='home_page'),
    url(r'^feed/new/post$',views.new_post,name='new_post'),
    url(r'^feed/post/(\d+)',views.post,name ='post'),
]

