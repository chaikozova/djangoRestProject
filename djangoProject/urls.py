"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog_app import views1
from lesson1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/v1/courses/', views.get_all_courses),
    path(r'api/v1/courses/<int:id>/', views.get_course),
    path(r'api/posts', views1.get_all_posts),
    path(r'api/posts/<int:id>/', views1.get_post),
    #path('', include('blog_app.urls')),
    #url(r'^api/v1/course/', views.get_all_course),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
