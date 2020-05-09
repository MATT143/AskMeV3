from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    CATEGORY_CHOICES = (
        ('sap', 'SAP'),
        ('java', 'JAVA'),
        ('python', 'PYTHON'),
        ('testing', 'TESTING'),
        ('select category', 'SELECT CATEGORY')
    )
    ROLE_CHOICES=(
        ('Approver','APPROVER'),
        ('Consultant', 'CONSULTANT')


    )
    user=models.OneToOneField(User,on_delete=models.CASCADE,)
    category=models.CharField(max_length=30,choices=CATEGORY_CHOICES,default='select category')
    user_role=models.CharField(max_length=30,choices=ROLE_CHOICES,default='Consultant')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)



