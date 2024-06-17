from django.db import models
from PIL import Image

class Users(models.Model):
    login = models.CharField(max_length=5, null=False)
    password = models.CharField(max_length=5)
    avatar = models.ImageField(upload_to='images/')


class Path(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    length = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    hotel_Main_Img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    x1 = models.CharField(max_length=30, default="0")
    x2 = models.CharField(max_length=30, default="0")
    y1 = models.CharField(max_length=30, default="0")
    y2 = models.CharField(max_length=30, default="0")


    def count_product(self):
        return Favorites.objects.filter(path__pk=self.pk).count()

    def count_comment(self):
        return Comments.objects.filter(path__pk=self.pk).count()


class Comments(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)


class Favorites(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)