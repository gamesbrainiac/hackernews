from urlparse import urlparse

from django.db import models
import django.contrib.auth.models as auth_models


class Story(models.Model):
    # Database columns
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    moderator = models.ForeignKey(auth_models.User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Properties
    @property
    def domain(self):
        return urlparse(self.url).netloc

    # Methods
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'stories'
        ordering = ['-updated', 'title']