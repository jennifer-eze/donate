from django.db import models
from PIL import Image

# Create your models here.
class StartFund(models.Model):
    name = models.CharField(max_length=150, null=True)
    fundReason = models.CharField(max_length=500, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)