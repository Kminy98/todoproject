from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.TodoList.as_view(), name="TodoList"),
    path('<int:todo_id>/', views.TodoDetail.as_view(), name="TodoDetail"),

]
