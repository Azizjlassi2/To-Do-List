from django.urls import path
from . import views

urlpatterns = [

    path("api/" , views.getAllEndPoints),
    path('api/tasks/', views.task_list_api, name='task-list-api'),
    path('api/tasks/<int:task_id>/', views.task_detail_api, name='task-detail-api'),
    path('api/tasks/create/', views.create_task_api, name='create-task-api'),
    
    path('api/categories/', views.category_list_api, name='category-list-api'),
    path('api/categories/create/', views.create_category_api, name='create-category-api'),
]
