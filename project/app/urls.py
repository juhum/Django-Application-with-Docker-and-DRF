from django.urls import path, include

from app import views

urlpatterns = [
    path('tasks/', views.TaskView.as_view()),
    path('category/', views.CategoryView.as_view()),
]