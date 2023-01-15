from django.urls import path, include
from .views import home, add_todo, complete, delete_todo, ongoing
urlpatterns = [
    path('', home, name="home"),
    path('add/', add_todo, name="add todo" ),
    path('complete/<int:todo_id>/', complete),
    path('delete_todo/<int:todo_id>/', delete_todo),
    path('ongoing/<int:todo_id>/', ongoing)
]