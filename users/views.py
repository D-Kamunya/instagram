from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from .email import send_welcome_email
# Create your views here.


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

