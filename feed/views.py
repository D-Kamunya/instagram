from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_page(request):
  
  profile=Profile.get_profile_by_userid(request.user.id)
  print(profile.user.username)
  return render(request,'feed/home.html',{'profile':profile})
