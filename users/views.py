from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
# Create your views here.


def register_user(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home_page')
  else:
      form = SignUpForm() 
  return render(request, 'registration/registration_form.html', {'form': form})

