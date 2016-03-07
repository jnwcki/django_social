from django.contrib import admin

# Register your models here.
from socialapp.models import Post, UserProfile

admin.site.register(Post)
admin.site.register(UserProfile)
