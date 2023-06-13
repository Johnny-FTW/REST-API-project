from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAAPIView.as_view())
]