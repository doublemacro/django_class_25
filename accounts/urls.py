from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

