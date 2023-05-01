from django.db import models
from user.models import User, UserManager


# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='todos') 
    title = models.CharField(max_length=100, null=False)
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    completion_at = models.DateTimeField(default=False, null=True, blank=True)


    #타이틀로 뜨게함?
    def __str__(self):
        return str(self.title)
        # return self.title