from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="homepage"),
    path("delconf/<str:pk>/",views.delete_confirm,name="delete-confirmation"),
    path("del/<str:pk>/",views.main_del,name="delete"),
    path("clear-all",views.clearAll,name="clear-all"),
    path("all_del/<int:user_id>/",views.deleteAll,name="all_del"),
    #api
    path("signup",views.sign_up_user,name="user-singup")
]
