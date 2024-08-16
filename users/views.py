from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # saves user to database
            form.save()
            username = form.cleaned_data.get('username')
            # Flash message that appears for account creation confirmation and disappears
            messages.success(request, f'Your account has been! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Decorators add functionality to existing function
# login_required user must be logged in to view page
@login_required
def profile(request):
    return render(request, 'users/profile.html')

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
