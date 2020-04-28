from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
	# Home page
	path('todoapp/', views.todoappView, name='todoappView'),
    path('addTodoItem/', views.addTodoItem, name='addTodoItem'),
    path('deleteTodoItem/<int:i>/', views.deleteTodoItem, name='deleteTodoItem'),
]
