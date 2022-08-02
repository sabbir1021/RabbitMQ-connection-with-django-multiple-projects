from django.urls import path, include
from . import views

urlpatterns = [
    path('comments/', views.CommentListCreate.as_view(),name='comments')
]