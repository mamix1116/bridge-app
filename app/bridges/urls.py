from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bridges'),
    path('<int:bridges_id>', views.bridge, name='bridge'),
    path('search', views.search, name='search'),
]
