# Signal fired after and objecct gets saved
from django.db.models.signals import post_save
# Get post_Save signal when user is created, the sender
from django.contrib.auth.models import User
# Receiver gets signal and performs a task
from django.dispatch import receiver
# Create a new profile for each new user
from .models import Profile

# When a user is created send the signal
# The receiver is the create_profile function
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# When a user is saved send the signal
# The receiver is the save_profile function
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()