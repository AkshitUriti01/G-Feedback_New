from django.urls import path
from . import views

app_name = "feedbackapp"
urlpatterns = [
    path("", views.apply, name="apply"),
    path("login/", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("logout/", views.logout, name="logout"),
    path("view/<str:id>", views.view, name="view"),
]
