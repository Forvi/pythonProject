from .models import *
from PIL import Image

def registration(login, password):
    new_user = Users.objects.filter(login=login)
    if len(new_user) != 0:
        return False
    new_user = Users(login=login, password=password)
    new_user.save()
    return True

def loginacc(login, password):
    print("успешно")
    user = Users.objects.filter(login=login, password=password)
    if len(user) != 0:
        return user[0].pk
    return False

def all_path():
    paths = Path.objects.all()
    return paths

def pagePath(pk):
    path = Path.objects.filter(pk=pk)
    return path[0]

def path_user(user_id):
    user = Path.objects.filter(author=user_id)
    return user

def get_user_on_pk(user_id):
    return Users.objects.get(pk=user_id)

def check_on_auto(user_id):
    if user_id:
        return True
    return False