from rest_framework import viewsets, mixins

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    #ALL 4 METHODS


class ProductGenericViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    #get, set + detail

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

