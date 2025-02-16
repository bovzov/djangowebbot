from django.urls import path
from .views import product_list, chekout


urlpatterns = [
    path('', product_list, name='product_list'),
    path('checkout/', chekout, name='checkout'),   

]