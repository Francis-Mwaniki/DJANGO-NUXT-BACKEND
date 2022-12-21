from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User

class Cook(models.Model):
    cookName = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    recipeName = models.CharField(max_length=255)
    quote = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.cookName
    def __str__(self):

        return self.host.get_username()    

    def __str__(self):
        return self.recipeName
    

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class Customer(models.Model):
    customername = models.CharField(max_length=255,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cook = models.ForeignKey(Cook, on_delete=models.SET_NULL,null=True)
    rating = models.IntegerField()
    comments = models.TextField(blank=True,null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self):
        return self.customername
    def __str__(self):
        return self.user.get_username()
    def __str__(self):
        return self.cook

    def __str__(self):
        return self.rating

    def __str__(self):
        return self.comments
 
