from django.urls import path
from .views import home, todoAdd, todoDetails

app_name = 'todo'


urlpatterns = [
    path('', home, name="home"),
    path('add/', todoAdd, name="add"),
    path('detail/<int:pk>/', todoDetails, name="todo-detail")
]