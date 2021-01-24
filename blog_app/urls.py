from django.contrib import admin
from django.urls import path
from blog_app import views1

urlpatterns = [
    path(r'api/v1/posts', views1.get_all_posts),
    path(r'api/v1/posts/<int:id>/', views1.get_post),

]

