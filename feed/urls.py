from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.home_page,name='home_page'),
    url(r'^feed/new/post$',views.new_post,name='new_post'),
    url(r'^feed/post/(\d+)/like',views.like_post,name ='like_post'),
    url(r'^feed/post/(\d+)/delete',views.delete_post,name ='delete_post'),
    url(r'^feed/post/(\d+)',views.post,name ='post'),
    url(r'^feed/post/favourites',views.favourite_posts,name ='favourite_posts'),
    url(r'feed/search/', views.search_posts, name='search_posts'),
]

