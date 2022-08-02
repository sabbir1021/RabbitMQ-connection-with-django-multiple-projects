from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', views.CategoryListCreate.as_view(), name='category'),
    path('blog/', views.BlogListCreate.as_view(),name='blog'),
    path('comments/', views.CommentListCreate.as_view(),name='comments')
]