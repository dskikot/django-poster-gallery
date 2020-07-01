from django.urls import path
from .views import IndexList, ImagesByCategory, ImagesByTag, ImageDetail

urlpatterns = [
    path('', IndexList.as_view(), name='home'),
    path('category/<str:slug>/', ImagesByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', ImagesByTag.as_view(), name='tag'),
    path('image/<int:pk>/', ImageDetail.as_view(), name='image')
]
