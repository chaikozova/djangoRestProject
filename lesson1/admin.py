from django.contrib import admin

# Register your models here.
from lesson1.models import Course, Student
from blog_app.models import Post, Comment

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Comment)

