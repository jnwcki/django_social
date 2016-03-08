from django.contrib import admin

# Register your models here.
from socialapp.models import Post, UserProfile, Tag

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Tag)