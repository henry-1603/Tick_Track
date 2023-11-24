
from django.urls import path
from .views import TaskList , TaskCreate , TaskUpdate , TaskDelete , CustomLoginView 
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("login/" , CustomLoginView.as_view() , name="login"),
    path("logout/" , LogoutView.as_view(next_page = 'login') , name="logout"),

    path("register/" , views.registerPage , name="register"),
    
    
    
    path("" , TaskList.as_view() , name="tasks"),
    path("task-create/" , TaskCreate.as_view() , name="task-create"),
    path("task-update/<int:pk>/" , TaskUpdate.as_view() , name="task-update"),
    path("task-delete/<int:pk>/" , TaskDelete.as_view() , name="task-delete"),

    
]
