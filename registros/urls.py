from django.urls import path
from .views import list_registro, delete_registro, update_registro, new_registro, pesquisa
from django.contrib.auth import views as auth_views

app_name = 'registros'

urlpatterns = [
    path('list_registro/', list_registro, name='list_registro'),
    path('new/', new_registro, name='new_registro'),
    path('update/<int:pk>/', update_registro, name='update_registro'),
    path('delete/<int:pk>/', delete_registro, name='delete_registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('buscar/', pesquisa, name='pesquisa'),
]