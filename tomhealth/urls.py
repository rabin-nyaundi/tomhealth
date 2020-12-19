from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id>/product/', views.product_view, name='product'),
    path('<int:id>/index/', views.search_view, name='search')
]