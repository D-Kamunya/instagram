from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import Image
from .forms import NewImageForm
from users import views as user_views
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_page(request):
  following=user_views.get_following(request)
  following_posts=[]
  all_posts=Image.get_all_images()
  for post in all_posts:
    if post.profile in following:
      following_posts.append(post)
  profile=Profile.get_profile_by_userid(request.user.id)
  my_posts=Image.filter_by_userid(request.user.id)
  context={
    'profile':profile,
    'following':following,
    'all_posts':all_posts,
    'following_posts':following_posts,
    'my_posts':my_posts
  }
  return render(request,'feed/home.html',context)



@login_required(login_url='/accounts/login/')
def new_post(request):
    current_profile = request.user.profile
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_profile
            image.save()
        return redirect('home_page')

    else:
        form = NewImageForm()
    context={
      'profile':current_profile,
      'form':form
    }    
    return render(request, 'feed/new_image.html',context)