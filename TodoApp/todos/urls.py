from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('register/', RegisterPage.as_view(),name='register'),

    path('list/',views.list_todo_items, name='items'),
    path('insert_todo/',views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/',views.delete_todo_item, name='delete_todo_item'),
]