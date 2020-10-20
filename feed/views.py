from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from django.db.models import F
from .models import Image,Like,Image_Comment
from .forms import NewImageForm,NewCommentForm
from users import views as user_views
# Create your views here.

def get_liked_posts(request):
  liked_posts=Like.objects.filter(user=request.user)
  return liked_posts


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
        return redirect('my_profile')

    else:
        form = NewImageForm()
    context={
      'profile':current_profile,
      'form':form
    }    
    return render(request, 'feed/new_image.html',context)



@login_required(login_url='/accounts/login/')
def post(request,post_id):
  post=Image.get_image_by_id(post_id)
  posts_liked=[]
  post_comments=Image_Comment.objects.filter(image=post)
  for like in get_liked_posts(request):
    posts_liked.append(like.post)


  if request.method == "POST":
        comment_form = NewCommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.profile = Profile.get_profile_by_userid(request.user.id)
            comment.image = post
            comment.save()
            comment_form = NewCommentForm()
            Image.objects.filter(id=post_id).update(comments=F("comments") + 1)  
            return redirect("post", post_id)
  else:
      comment_form = NewCommentForm()
  context={
    'profile':request.user.profile,
    'post':post,
    'posts_liked':posts_liked,
    'form':comment_form,
    'comments':post_comments

  }
  return render(request, 'feed/post.html',context)



@login_required(login_url='/accounts/login/')
def like_post(request,post_id):
  post=Image.get_image_by_id(post_id)
  user=request.user
  like = Like.objects.filter(user=user, post=post)
  if like:
    like.delete()
    Image.objects.filter(id=post_id).update(likes=F("likes") - 1)
  else:
    Like.objects.create(user=user,post=post)
    Image.objects.filter(id=post_id).update(likes=F("likes") + 1)  

  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def delete_post(request,post_id):
  Image.delete_image(post_id)
  return redirect('my_profile')