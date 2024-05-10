from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'categories', CategoryViewset)
router.register(r'orders', OrderViewset)

app_name = 'shop'

urlpatterns = [
    path('api/', include(router.urls)),  
    path('cart/', cart_detail, name="cart_detail"),
    path('cart/add/<int:product_id>', cart_add, name="cart_add"),
    path('orders/create/', order_create, name="order_create"),
    path('cart/remove/<int:product_id>', cart_remove, name="cart_remove"),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
]
