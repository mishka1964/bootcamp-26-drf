from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add =True)
    uploated_at = models.DateTimeField(auto_now_add =False)

    def __str__(self):
        return self.title