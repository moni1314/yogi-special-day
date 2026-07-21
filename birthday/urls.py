from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('letter/', views.letter, name='letter'),
    path('gallery/', views.gallery, name='gallery'),
    path('video/', views.video, name='video'),
    path('cake/', views.cake, name='cake'),
    path('final/', views.final, name='final'),
    path("video/", views.video, name="video"),
    path("gift/", views.gift, name="gift"),
    path("family/", views.family, name="family"),
    path("certificate/", views.certificate, name="certificate"),
]