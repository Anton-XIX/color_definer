from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .custom_functions import get_image_color
user = get_user_model()


class UserImage(models.Model):
    user = models.ForeignKey(user, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m.%d/', null=True, blank=True)
    upload_date = models.DateTimeField(default=timezone.now())
    color = models.CharField(max_length=255, default='Not defined')

    def save(self, *args, **kwargs):
        self.color =  get_image_color(self.image)
        super(UserImage, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} - {self.image.name}'


