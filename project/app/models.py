from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    purpose = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    percentage_throughout = models.CharField( max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None,default='default_photo.jpg')

    def __str__(self):
        return self.name
    