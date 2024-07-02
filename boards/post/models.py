from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=40)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
