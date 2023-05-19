from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import os

from liqpay import LiqPay
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import random
import requests

public_key=os.getenv('PAYMENTS_PUBLIC_KEY')
privat_key=os.getenv('PAYMENTS_SECRET_KEY')

# class PayView(TemplateView):
#     template_name = 'create.html'

#     def get(self, request, *args, **kwargs):
        
#         liqpay = LiqPay(public_key, privat_key)
#         cart = Cart(request)
#         amount=str(cart.get_total_price())
#         # OrderItem.objects.create(        order=order,
#         #                                  product=item['product'],
#         #                                  price=item['price'],
#         #                                  quantity=item['quantity'])
#         # очистка корзины
#         # cart.clear()
#         params = {
#             'action': 'pay',
#             'amount': amount,
#             'currency': 'UAH',
#             'description': 'Payment for clothes',
#             'order_id': random.randint(1, 1000),
#             'version': '3',
#             'sandbox': 1, # sandbox mode, set to 1 to enable it
#             # 'server_url': '91.219.62.248/223', # url to callback view
#             'result_url': 'http91.219.62.248/123',
#         }
#         signature = liqpay.cnb_signature(params)
#         data = liqpay.cnb_data(params)
#         # print(request.POST.items)
#         return render(request, self.template_name, {'signature': signature, 'data': data})

@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(public_key, privat_key)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(public_key + data + privat_key)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('121212')
        print('callback data', response)
        return render(request, 'created.html',
                  {'order': response})
        # return HttpResponse()

def order_create(request):
    cart = Cart(request)
    # public_key=os.getenv('PAYMENTS_PUBLIC_KEY')
    # privat_key=os.getenv('PAYMENTS_SECRET_KEY')
    print(privat_key)
    cart = Cart(request)
    amount=str(cart.get_total_price())
    liqpay = LiqPay(public_key, privat_key)
    html = liqpay.cnb_form({
        'action': 'pay',
        'amount': amount,
        'currency': 'UAH',
        'description': 'description text',
        'order_id': random.randint(1, 100),
        'version': '3',
        'result_url': 'http://91.219.62.248/create/pay-callback/',
    })
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'create.html',
                  {'cart': cart, 'form': form, 'html':html})