from django.contrib import admin
from django.db import models
from . models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','disc']
