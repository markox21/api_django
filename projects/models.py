from django.db import models

# Create your models here.
class Project(models.Model):
    email = models.EmailField(max_length=200)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title