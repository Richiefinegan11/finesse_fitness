from profiles.models import UserProfile
from django.db import models


class Blog(models.Model):
    """
    Creates a blog type model
    """

    title = models.CharField(max_length=120)
    blog_content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    comments  = models.TextField()
    user = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
