from django.urls import path
# from .views import PayView, PayCallbackView
from .views import  PayCallbackView
from . import views

app_name = 'orders' 

urlpatterns = [
    path('', views.order_create, name='order_create'),
    # path('', PayView.as_view(), name='order_create'),
    path('pay-callback/', PayCallbackView.as_view(), name='pay_callback')

]