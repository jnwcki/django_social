from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOICES = [('h', 'Hiking'),
           ('r', 'Running'),
           ('b', 'Mountain Biking'),
           ('c', 'Climbing'),
           ('s', 'Skiing')
           ]


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField()
    activity = models.CharField(max_length=30, choices=CHOICES)
    user = models.ForeignKey('auth.User')
    post_time = models.DateTimeField(auto_now_add=True)
    post_tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-post_time"]

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    screen_name = models.CharField(max_length=50)
    likes = models.ManyToManyField(Post, related_name="user_likes")
    friends = models.ManyToManyField('auth.User', related_name='friend')

    def __str__(self):
        return self.screen_name


@receiver(post_save, sender="auth.User")
def user_profile_create(sender, **kwargs):
    created = kwargs.get("created")
    if created:
        instance = kwargs.get("instance")
        UserProfile.objects.create(user=instance)




