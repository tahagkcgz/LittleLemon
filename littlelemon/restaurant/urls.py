from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuView.as_view(), name='menuview'),
    path('menu/<int:pk>', views.SingleMenuView.as_view(), name='single_menuview'),
    path('api-token-auth/', obtain_auth_token),
]
