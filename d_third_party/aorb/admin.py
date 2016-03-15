from django.contrib import admin

# Register your models here.
from .models import Pair, Choice

admin.site.register(Pair)
admin.site.register(Choice)
