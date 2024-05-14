from pathlib import Path

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .basa import *
import re

from django.http import JsonResponse

def check_login_status(request):
    is_authenticated = request.user.is_authenticated
    return JsonResponse({'is_authenticated': is_authenticated})

class Registration(View):

    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        password = request.POST.get("password")
        login = request.POST.get("login")
        error_message = ''

        if check_password(password):
            print("Успешно")
        else:
            error_message = "Недопустимые символы"

        if check_login(login):
            print("Успешно")
        else:
            error_message = "Недопустимые символы"

        if len(password) < 5:
            error_message = "Пароль должен быть более 5 символов"

        elif len(login) < 5:
            error_message = "Логин должен быть более 5 символов"
        if error_message != '':
            context = {
                'error_message': error_message
            }
            return render(request, 'registration.html', context=context)
        else:
            if registration(login, password):
                return HttpResponseRedirect('signup')
            else:
                error_message = "Пользователь с таким логином уже существует"
                context = {
                    'error_message': error_message
                }
                return render(request, 'registration.html', context=context)

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login = request.POST.get("login2")
        password = request.POST.get("password2")

        pk = (loginacc(login, password))
        if pk:
            request.session['user'] = pk
            return HttpResponseRedirect('main')
        else:
            error_message = "Пользователь не найден"
            context = {
                'error_message': error_message
            }
            return render(request, 'login.html', context=context)


def check_password(password):
    pattern = re.compile('^[A-Za-z0-9]+$')
    if re.match(pattern, password):
        return True
    else:
        return False

def check_login(login):
    pattern = re.compile('^[A-Za-z0-9]+$')
    if re.match(pattern, login):
        return True
    else:
        return False

class Main(View):
    def get(self, request):


        paths = all_path()
        context = {
            'paths': paths
        }
        return render(request, 'main.html', context=context)

#adsada
class Redactor(View):
    def get(self, request):
        return render(request, 'redactor.html')

    def post(self, request):
        form = Path(length=request.POST.get('path'),
                    hotel_Main_Img=request.FILES.get('image'),
                    name=request.POST.get('name'),
                    text=request.POST.get('text'),
                    author=get_user_on_pk(request.session.get('user')))
        form.save()
        return HttpResponseRedirect('main')

class PagePath(View):
    def get(self, request, pk):

        context = {
            'path': pagePath(pk),
            'author_id': request.session.get("user"),
            'comment': Comments.objects.filter(path_id=pk),
        }
        print(Comments.objects.filter(path_id=pk))
        return render(request, 'path.html', context=context)

    def post(self, request, pk):
        path = Path.objects.get(id=pk)
        text_area = request.POST.get('text')
        length = request.POST.get('length')
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if len(text_area) != 0:
            path.text_area = text_area
        if len(length) != 0:
            path.length = request.POST.get('length')
        if len(name) != 0:
            path.name = request.POST.get('name')
        if image is not None:
            path.hotel_Main_Img = image
        path.save()
        return HttpResponseRedirect('../path/'+str(pk))

class Profile(View):
    def get(self, request):
        user_id = request.session.get("user")
        context = {
            'paths': path_user(user_id)
        }
        return render(request, 'profile.html', context=context)

def del_path(request, pk):
    delete_path = Path.objects.get(pk=pk)
    delete_path.delete()
    return HttpResponseRedirect('../profile')

def create_comment(request, pk):
    user = get_user_on_pk(request.session.get("user"))
    path = Path.objects.get(pk=pk)
    text_comment = request.GET.get('text_comment')
    print(text_comment)
    Comments(text=text_comment, path=path, author=user).save()
    return JsonResponse({
    })

class CheckUserView(View):
    def post(self, request):
        if request.user.is_authenticated:
            return JsonResponse({'is_authenticated': True})
        else:
            return JsonResponse({'is_authenticated': False, 'error_message': 'Войдите в аккаунт'})
