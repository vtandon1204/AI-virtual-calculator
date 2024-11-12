from django.contrib import admin
from django.urls import path
from calc_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('get_response/', views.get_response, name='get_response'),
]
