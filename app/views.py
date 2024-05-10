from app.serializers import *
from app.models import *
from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from .cart import Cart
from .forms import *


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(['GET', 'POST'])
def product_list(request, format=None, category_slug=None):
    if request.method == 'GET':
        employeis = Product.objects.all()
        serializer = ProductSerializer(employeis, many=True)

        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('success', safe=False)
        return JsonResponse('errors', safe=False)

@api_view(['GET'])
def product_detail(request, pk):
    employee = Product.objects.get(id=pk)
    serializer = ProductSerializer(employee)

    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.data)
    if form.is_valid():
        cd = form.validated_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def cart_detail(request):
    cart = Cart(request)
    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(['POST'])
def order_create(request):
    cart = Cart(request)
    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'], price=item['price'])
        cart.clear()
        return Response(OrderSerializer(order).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)