import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lesson1.serializer import CourseSerializer
from lesson1.models import Course


@api_view(['GET'])
def get_all_courses(request):
    courses = Course.objects.all()
    data = CourseSerializer(courses, many=True).data
    return Response(data=data)


@api_view(['GET'])
def get_course(request, id):
    try:
        courses = Course.objects.get(id=id)
    except Course.DoesNotExist:
        return Response(data={'result': 'item not found'}, status=status.HTTP_404_NOT_FOUND)
    data = CourseSerializer(courses).data
    return Response(data=data)


def get_all_course(request):
    courses = []
    for i in Course.objects.all():
        courses.append(model_to_dict(i))
    print(courses)
    json_data = json.dumps(courses)
    return HttpResponse(json_data)
