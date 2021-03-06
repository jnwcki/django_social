from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.db import IntegrityError
from django.views.generic import CreateView, TemplateView, View, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from socialapp.models import UserProfile, Post, Tag


class NewUserCreation(UserCreationForm):
    screen_name = forms.CharField()


class UserCreateView(CreateView):
    model = User
    form_class = NewUserCreation

    def form_valid(self, form):
        new_user = form.save()
        new_user_screen_name = form.cleaned_data.get('screen_name')
        new_user.userprofile.screen_name = new_user_screen_name
        new_user.userprofile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('login')


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = Post.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        t_search = request.POST.get('tag_search')
        search_true = "Search Results:"
        results = []
        if t_search:
            results = Post.objects.filter(post_tags__name__contains=t_search)
        return render(request, 'index.html', {"object": results,
                                              "search_true": search_true
                                              }
                      )


class CreatePostView(CreateView):
    model = Post

    fields = ['title', 'blog', 'activity', 'post_tags']

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class LikePost(View):

    def get(self, request, pk):

        user_p = UserProfile.objects.get(user=self.request.user)
        try:
            user_p.likes.add(pk)
            return HttpResponseRedirect(reverse('index'))

        except IntegrityError:
            return HttpResponseRedirect(reverse('index'))


class LikeAuthor(View):

    def get(self, request, pk):
        user_p = UserProfile.objects.get(user=self.request.user)
        try:
            user_p.friends.add(pk)
            return HttpResponseRedirect(reverse('index'))

        except IntegrityError:
            return HttpResponseRedirect(reverse('index'))


class MyLikes(View):
    def get(self, request):
        user = UserProfile.objects.get(user=self.request.user)
        return render(request, 'socialapp/userprofile_list.html', {'user': user})


class AuthorView(DetailView):
    model = UserProfile


class PostDetailView(View):

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        tags = Tag.objects.all()

        return render(request, 'socialapp/post_detail_view.html',
                      {'post_detail': post,
                       'all_tags': tags}
                      )


class TagView(CreateView):
    model = Tag
    fields = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        return context

    def get_success_url(self):
        return reverse('tags')