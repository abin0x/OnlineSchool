from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_teacher = models.BooleanField(default=True)
    # profile_image = models.ImageField(upload_to='users_images', blank=True, null=True)
    profile_image = models.URLField(max_length=500, null=True, blank=True)
    # image = models.URLField(max_length=500, null=True, blank=True)

