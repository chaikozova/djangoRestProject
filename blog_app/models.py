from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='posts/', null=True)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}:, {self.description}, {self.date_added}'


class Comment(models.Model):
    comment = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='comments')