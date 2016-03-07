from django.db import models

# Create your models here.

CHOICES = [('h', 'Hiking'),
           ('r', 'Running'),
           ('b', 'Mountain Biking'),
           ('c', 'Climbing'),
           ('s', 'Skiing')
           ]


class Post(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField()
    activity = models.CharField(max_length=30, choices=CHOICES)
    user = models.ForeignKey('auth.User')
    post_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-post_time"]

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    screen_name = models.CharField(max_length=50)
    likes = models.ManyToManyField(Post)
    friends = models.ManyToManyField('self', related_name='friend')

    def __str__(self):
        return self.screen_name