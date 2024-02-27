from django.contrib import admin

from .models import Category, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
