from django.db import models
from django.contrib.auth.models import User


class Foo(models.Model):
    """
    A silly model for demonstration
    """
    title = models.CharField(max_length=30, blank=True, null=True)
    body = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return ' '.join(str(self.pk), self.title)
