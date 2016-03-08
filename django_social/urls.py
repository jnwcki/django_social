"""django_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from socialapp.views import IndexView, UserCreateView, CreatePostView, LikePost, LikeAuthor, MyLikes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^createuser/', UserCreateView.as_view(), name="create_user"),
    url(r'login/', auth_views.login, name='login'),
    url(r'logout', auth_views.logout_then_login, name='logout'),
    url(r'create', CreatePostView.as_view(), name='create'),
    url(r'like_post/(?P<pk>\d+)', LikePost.as_view(), name="like_post"),
    url(r'like_author/(?P<pk>\d+)', LikeAuthor.as_view(), name="like_author"),
    url(r'my_likes/', MyLikes.as_view(), name='my_likes')
]
