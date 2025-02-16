from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product

def product_list(request):
    products = Product.objects.all().values('id', 'name','price')
    return JsonResponse(list(products), safe=False)

@csrf_exempt
def chekout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'status': 'success', 'products': data.get('products', [])})
    
    
