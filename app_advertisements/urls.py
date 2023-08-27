from django.urls import path
from .views import basic_view

urlpatterns = [
    path('', basic_view("index"), name = 'main-page'),
    path('top-sellers/', basic_view("top-sellers"), name = 'top-sellers'),
    path('advertisement-post/', basic_view("advertisement-post"), name = 'advertisement-post'),
    path('register/', basic_view("register"), name = 'register'),
    path('login/', basic_view("login"), name = 'login'),
    path('profile/', basic_view("profile"), name = 'profile')
]

