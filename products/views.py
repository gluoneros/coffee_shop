from django.shortcuts import render
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.forms import ProductForm
from django.urls import reverse_lazy
from products.models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductFormView(generic.FormView):
    template_name = "products/add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListView(generic.ListView):
    template_name = "products/list_product.html"
    model = Product
    context_object_name = "products"
    reverse_lazy("list_product")


# Inclusion del petodo get de la  API para la lista de productos


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk=None, format=None):
        id = pk

        if id is not None:
            try:
                product_id = Product.objects.get(id=id)
                serializer = ProductSerializer(product_id)
                return Response(serializer.data)
            except Exception as error:
                return Response(
                    {"msg": "Product Was not found"}, status=status.HTTP_404_NOT_FOUND
                )

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, pk=None, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Product Created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        try:
            product_id = Product.objects.get(pk=id)
            serializer = ProductSerializer(product_id, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"msg": "Product Updated"}, status=status.HTTP_201_CREATED
                )

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(
                {"msg": "Product Was not found"}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk=None, format=None):
        id = pk
        try:
            product_id = Product.objects.get(pk=id)
            product_id.delete()
            return Response({"msg": "Product Deleted"}, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(
                {"msg": "Product Was not found"}, status=status.HTTP_404_NOT_FOUND
            )
