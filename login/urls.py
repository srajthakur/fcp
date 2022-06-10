from django.urls import path
from .import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('use_camera', views.use_camera, name='use_camera'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('', views.login, name='login'),


]