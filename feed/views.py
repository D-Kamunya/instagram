from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .forms import NewImageForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def home_page(request):
  
  profile=Profile.get_profile_by_userid(request.user.id)
  context={
    'profile':profile
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