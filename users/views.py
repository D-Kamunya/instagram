from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import SignUpForm,UserProfileForm,EditProfileForm
from django.contrib.auth import login, authenticate
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .models import Profile
from feed.models import Image
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block
# Create your views here.
@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def get_following(request):
  all_profiles=Profile.get_all_profiles(request.user)
  following=Follow.objects.following(request.user)
  following_id=[]
  for followin in following:
    following_id.append(followin.id)
  following=[]
  for profile in all_profiles:
    if profile.user.id in following_id:
      following.append(profile)
  return following 

@login_required(login_url='/accounts/login/')
def get_followers(request):
  all_profiles=Profile.get_all_profiles(request.user)
  followers=Follow.objects.followers(request.user)
  followers_id=[]
  for follower in followers:
    followers_id.append(follower.id)
  followers=[]
  for profile in all_profiles:
    if profile.user.id in followers_id:
      followers.append(profile)
  return followers    



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


@login_required(login_url='/accounts/login/')
def  add_following(request,follow_id):
  following_user=User.objects.get(pk=follow_id)
  Follow.objects.add_follower(request.user, following_user)
  return redirect('not_following')

@login_required(login_url='/accounts/login/')
def remove_following(request,follow_id):
  following_user=User.objects.get(pk=follow_id)
  Follow.objects.remove_follower(request.user, following_user)
  return redirect('my_profile')

@login_required(login_url='/accounts/login/')
def my_profile(request):
  profile=request.user.profile
  following=get_following(request)
  followers=get_followers(request)
  my_posts=Image.filter_by_userid(request.user.id)
 
  context={
    'profile':profile,
    'following':following,
    'followers':followers,
    'posts':my_posts
  }
  return render(request, 'users/my_profile.html',context)




@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('my_profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
        context={
          'form':form,
          'profile_form':profile_form,
          'profile':request.user.profile
        }
        return render(request, 'users/edit_profile.html',context)