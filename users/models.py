# Need to migrate model changes to take effect in the database
# Run commands in terminal:
#   python manage.py makemigrations (creates the migrations)
#   python manage.py migrate (applies changes to the database)
# Register models to admin.py file in the app to view models in admin page of website
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
