from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=5, null=False)
    password = models.CharField(max_length=5)

class Path(models.Model):
    name = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    length = models.IntegerField()
    hotel_Main_Img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

class Comments(models.Model):
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
