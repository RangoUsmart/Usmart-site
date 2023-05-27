#users/urls.py
from django.urls import path, re_path
from . import views
# from projects import views as v2

app_name = 'rezume' 
urlpatterns = urlpatterns = [
    path('', views.RezumeView.as_view(), name='cv'),
    path('edit/', views.cv_edit, name='cv_edit'),
]

