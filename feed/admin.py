from django.contrib import admin
from .models import Image,Like,Image_Comment

# Register your models here.
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Image_Comment)