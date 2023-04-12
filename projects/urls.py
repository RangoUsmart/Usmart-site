#users/urls.py

from django.urls import path
from projects import views
  
urlpatterns = [
    path('', views.PostView.as_view()),
    path('<int:pk>/', views.PostProject.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),

]