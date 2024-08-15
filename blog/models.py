from django.db import models
from django.utils import timezone
# user is a separate table
# post model and user model will have a relationship
# user authors posts, one to many relationship
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length= 100) 
    content = models.TextField()
    # passes in the actual function as the defualt value
    date_posted = models.DateTimeField(default=timezone.now)
    # if a user is deleted, all their posts will be deleted as well
    # one way street, deletion of post does not delete user
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #Dunder (double underscores), shows title of post when printed in shell
    def __str__(self):
        return self.title