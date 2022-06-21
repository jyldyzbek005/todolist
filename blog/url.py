from django.urls import path
from .views import index, addToDo, complete_todo, delete_complate, delete_all
urlpatterns = [
    path('', index, name='index'),
    path('', index, name='index'),
    path('add', addToDo, name='add'),
    path('complate/<todo_id>', complete_todo, name='complete'),
    path('delete_complate', delete_complate, name='deletecomplate'),
    path('delete_all', delete_all, name='deleteall')
]
