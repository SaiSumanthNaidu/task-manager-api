from django.urls import path
from .views import (CreateTaskView,TaskListView,TaskDetailView,TaskUpdateView,TaskDeleteView
)
urlpatterns = [
    path('tasks/', CreateTaskView.as_view()),
    path('tasks/list/', TaskListView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view()),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view()),
]