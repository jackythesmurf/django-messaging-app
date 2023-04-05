from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.username
    
class Messages(models.Model):
    username_1 = models.CharField(max_length=50)
    username_2 = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.username_1} - {self.username_2}  - {self.content}'