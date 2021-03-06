from django.db.models.fields import DateTimeField
from profiles.models import UserProfile
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    """
    Creates a blog type model
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', null=True, blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
