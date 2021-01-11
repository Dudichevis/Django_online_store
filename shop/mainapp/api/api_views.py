from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, CustomerSerializer
from ..models import Category, Customer


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10

class CategoryListAPIView(ListAPIView):

    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()

class CustomerListAPIView(ListAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()



