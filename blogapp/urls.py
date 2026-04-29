from django.urls import path
from . import views

urlpatterns = [
    path('', views.lock_page, name='lock'),
    path('secret/', views.secret_page, name='secret'),
]
