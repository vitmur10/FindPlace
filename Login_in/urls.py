from django.urls import path
from . import views

app_name = 'Login_in'
urlpatterns = [
    path('', views.MainView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),

]
