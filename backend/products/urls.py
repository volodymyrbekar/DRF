from django.urls import path

from . import views

# api/products/
urlpatterns = [
    path('', views.product_list_crate_view),
    path('<int:pk>/', views.product_detail_view),
]
