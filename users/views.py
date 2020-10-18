from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
# Create your views here.

def get_not_following(request):
  all_profiles=Profile.get_all_profiles(request.user)
  following=Follow.objects.following(request.user)
  following_id=[]
  for followin in following:
    following_id.append(followin.id)
  not_following=[]
  for profile in all_profiles:
    if profile.user.id not in following_id:
      not_following.append(profile)
  return not_following



def register_user(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        send_welcome_email(username,email)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home_page')
  else:
      form = SignUpForm() 
  return render(request, 'registration/registration_form.html', {'form': form})



@login_required(login_url='/accounts/login/')
def not_following(request):
  
  not_following_profiles=get_not_following(request)
  prof=request.user.profile
  context={
    'profile':prof,
    'not_following':not_following_profiles
  }
  print(not_following_profiles)
  return render(request, 'users/not_following.html', context) 



def  add_following(request,follow_id):
  following_user=User.objects.get(pk=follow_id)
  Follow.objects.add_follower(request.user, following_user)
  return redirect('not_following')