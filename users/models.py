from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.width > 400 or img.height> 300:
                output_size = (100, 100)
                img.thumbnail(output_size)
                img.save(self.image.path)