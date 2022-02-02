#Django
from django.contrib.auth.models import User
from django.db import models

#Cloudinay
from cloudinary.models import CloudinaryField

#Models
from users.models import Profile

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = CloudinaryField('image')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} by @ {self.user.username}"