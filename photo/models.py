from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo_Album(models.Model):

    photo_Title = models.CharField(max_length=100)

    description = models.CharField(max_length=100)

    image = CloudinaryField('image')

    def __str__(self) -> str:
        return f"{self.photo_Title}"



