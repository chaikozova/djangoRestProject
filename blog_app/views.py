from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from django.forms import model_to_dict
from django.http import HttpResponse

from blog_app.serializer import PostSerializer, CommentSerializer
from blog_app.models import Post, Comment

# Create your views here.


@api_view(['GET'])
def get_all_posts(request):
    posts = Post.objects.all()
    data = PostSerializer(posts, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_post(request, id):
    try:
        posts = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(data={'result': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
    data = PostSerializer(posts).data
    return Response(data=data)