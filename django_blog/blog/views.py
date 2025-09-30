from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import CustomUserCreationForm, ProfileForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
    # automatically log in the user after registration
            login(request, user)
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('profile')
        else:
         messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})




@login_required
def profile(request):
    user = request.user
    profile = user.profile


    if request.method == 'POST':
        u_form = None
        p_form = ProfileForm(request.POST, request.FILES, instance=profile)
    # If you want to allow changing username/email, create a separate form for User
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile was updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
     p_form = ProfileForm(instance=profile)


    return render(request, 'registration/profile.html', {
    'p_form': p_form,
    })
