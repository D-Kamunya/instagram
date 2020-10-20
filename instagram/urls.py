"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from users import views as user_views
from django.contrib.auth import views 

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'',include('feed.urls')),
    url(r'^accounts/register',user_views.register_user,name='register_user' ),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}),
    url(r'^users/not-following/$',user_views.not_following,name='not_following'),
    url(r'^users/add/following/(\d+)$',user_views.add_following,name='add_following'),
    url(r'^users/remove/following/(\d+)$',user_views.remove_following,name='remove_following'),
    url(r'^users/my-profile/$',user_views.my_profile,name='my_profile'),
    url(r'^users/edit_profile/$',user_views.edit_profile, name ='edit_profile'),
    url(r'users/search/', user_views.search_users, name='search_users'),
]
