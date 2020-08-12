from django.contrib import admin
from phones.models import Phone
@admin.register(Phone)
class AdminPhone(admin.ModelAdmin):
    # отображение полей в админке
    list_display = ["id", "name", "price"]