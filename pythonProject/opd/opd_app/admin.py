from django.contrib import admin
from .models import *

admin.site.register(Users)
admin.site.register(Path)
admin.site.register(Comments)
admin.site.register(Favorites)