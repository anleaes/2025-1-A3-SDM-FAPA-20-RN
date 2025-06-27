from django.urls import path
from .views import CategoriaListCreate, CategoriaDetail

urlpatterns = [
    path('', CategoriaListCreate.as_view()),
    path('<int:pk>/', CategoriaDetail.as_view()),
]
