from django.contrib import admin
from django.urls import path, include
from opd_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth', Registration.as_view()),
    path('signup', Login.as_view()),
    path('main', Main.as_view()),
    path('redactor', Redactor.as_view()),
    path('path/<pk>', PagePath.as_view(), name="path"),
    path('profile', Profile.as_view()),
    path('del_path/<pk>', del_path, name="del_path"),
    path('check_user/', CheckUserView.as_view(), name='check_user'),
    path('create_comment/<pk>', create_comment, name='create_comment'),
    path('add_fav/<pk>', add_favorite, name="add_fav"),
    path('create_avatar', create_avatar, name="create_avatar"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
