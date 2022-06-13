# posts/urls.py
from django.urls import include, path

from . import views

app_name = 'posts'


urlpatterns = [
    #Главная страница
    path('', views.index, name='index'),
    #страница гроуплисn
    path('group/<slug:slug>/', views.group_posts, name='group'),
] 
