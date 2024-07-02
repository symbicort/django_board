from django.db import models
from user.models import User

class Post(models.Model):
    title = models.CharField(max_length=40)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True,blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
