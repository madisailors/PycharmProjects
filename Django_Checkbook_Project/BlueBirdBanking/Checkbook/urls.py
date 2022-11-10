from django.urls import path, include
from . import views

urlpatterns = [
    #sets the url path to home page index.html
    path('', views.home, name='index'),
    #sets the url path to create new account page
    path('create/', views.create_account, name='create'),
    path('<int:pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
]