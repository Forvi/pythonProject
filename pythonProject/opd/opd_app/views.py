from pathlib import Path
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
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
            'paths': paths,
            'user': get_user_on_pk(request.session.get("user"))
        }
        return render(request, 'main.html', context=context)


class Redactor(View):
    def get(self, request):
        user_id = request.session.get("user")
        check_on_auto(user_id)
        context = {
            'user': get_user_on_pk(user_id)
        }
        if not check_on_auto(user_id):
            return HttpResponseRedirect('signup')
        return render(request, 'redactor.html', context=context)

    def post(self, request):
        form = Path(length=request.POST.get('path'),
                    hotel_Main_Img=request.FILES.get('image'),
                    name=request.POST.get('name'),
                    text=request.POST.get('text'),
                    author=get_user_on_pk(request.session.get('user')),
                    x1=request.POST.get('X1'),
                    x2=request.POST.get('X2'),
                    y1=request.POST.get('Y1'),
                    y2=request.POST.get('Y2'))
        form.save()
        return HttpResponseRedirect('main')


class PagePath(View):
    def get(self, request, pk):
        context = {
            'path': pagePath(pk),
            'author_id': get_user_on_pk(request.session.get("user")),
            'comment': Comments.objects.filter(path_id=pk),
        }
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
        return HttpResponseRedirect('../path/' + str(pk))


class Profile(View):
    def get(self, request):
        user_id = request.session.get("user")
        check_on_auto(user_id)

        if not check_on_auto(user_id):
            return HttpResponseRedirect('signup')
        context = {
            'paths': path_user(user_id),
            'fav_paths': fav_path_user(user_id),
            'user': get_user_on_pk(user_id)
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
        user_id = request.session.get("user")
        if check_on_auto(user_id):
            return JsonResponse({'is_authenticated': True})
        else:
            return JsonResponse({'is_authenticated': False, 'error_message': 'Войдите в аккаунт'})


class Redact(View):
    def get(self, request, pk):
        user_id = request.session.get("user")
        check_on_auto(user_id)
        context = {
            'user': get_user_on_pk(user_id)
        }
        if not check_on_auto(user_id):
            return HttpResponseRedirect('signup')
        return render(request, 'redact.html', context=context)

    def post(self, request, pk):
        path = Path.objects.get(id=pk)
        text_area = request.POST.get('text')
        length = request.POST.get('length')
        print("?________")
        print(length)
        name = request.POST.get('name')
        image = request.FILES.get('image')
        x1 = request.POST.get('X1')
        x2 = request.POST.get('X2')
        y1 = request.POST.get('Y1')
        y2 = request.POST.get('Y2')

        if len(text_area) != 0:
            path.text_area = text_area
        if len(length) != 0:
            path.length = request.POST.get('length')
        if len(name) != 0:
            path.name = request.POST.get('name')
        if image is not None:
            path.hotel_Main_Img = image
        if len(x1) != 0:
            path.x1 = x1
        if len(x2) != 0:
            path.x2 = x2
        if len(y1) != 0:
            path.y1 = y1
        if len(y2) != 0:
            path.y2 = y2
        path.save()
        return HttpResponseRedirect('../path/' + str(pk))


def add_favorite(request, pk):
    user_id = request.session.get("user")
    check_on_add = Favorites.objects.filter(user=get_user_on_pk(user_id), path=pagePath(pk))
    if len(check_on_add) == 0:
        add_fav = Favorites(user=get_user_on_pk(user_id), path=pagePath(pk))
        add_fav.save()
    print(check_on_add)
    return JsonResponse({'is_authenticated': True})


def create_avatar(request):
    user_id = request.session.get("user")
    user_avatar = get_user_on_pk(user_id)
    user_avatar.avatar = request.FILES.get('avatar100')
    user_avatar.save()
    return HttpResponseRedirect('../profile')


def get_coords(request, pk):
    path = pagePath(pk)
    return JsonResponse({
        "x1": path.x1,
        "y1": path.y1,
        "x2": path.x2,
        "y2": path.y2,
        "center_x": str((float(path.x1) + float(path.x2)) / 2),
        "center_y": str(round((float(path.y1) + float(path.y2)) / 2, 7)),

    })
