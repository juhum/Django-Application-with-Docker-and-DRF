from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

from django.http import JsonResponse

class CategoryView(APIView):
    def get(self, request, format=None):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class TaskView(APIView):
    def get(self, request, format=None):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


def get_tasks_by_category(request, category_id):
    tasks = Task.objects.filter(category_id=category_id).values()
    return JsonResponse(list(tasks), safe=False)