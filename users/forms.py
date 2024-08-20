from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# inherits from UserCreationForm
class UserRegisterForm(UserCreationForm):
    # adds email field
    email = forms.EmailField()
    
    # nested namespace for configurations in one place
    class Meta:
        # affected model, eg. form.save() saves to user model
        model = User
        # fields in the form and in what order
        fields = ['username', 'email', 'password1', 'password2']
        

class UserUpdateForm(forms.ModelForm):
    # adds email field
    email = forms.EmailField()
    
    # nested namespace for configurations in one place
    class Meta:
        # affected model, eg. form.save() saves to user model
        model = User
        # fields in the form and in what order
        fields = ['username', 'email']
        

class ProfileUpateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']