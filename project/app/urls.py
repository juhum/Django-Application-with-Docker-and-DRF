from django.urls import path, include
from .views import get_tasks_by_category

from app import views

urlpatterns = [
    path('tasks/', views.TaskView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('tasks/category/<int:category_id>/', get_tasks_by_category, name='get_tasks_by_category'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),
        path('category/<int:pk>/', views.CategoryDetailView.as_view()),
]