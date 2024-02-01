from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import serializers
from . import models

# Create your views here.
@api_view(['GET'])
def customers(request):
    customers = models.Customer.objects.all().order_by('id')
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(customers, request)
    serializer = serializers.CustomerSerializer(result_page, many=True)
    data_response = {
        'status': "success",
        'total_data': paginator.page.paginator.count,
        'total_pages': paginator.page.paginator.num_pages,
        'current_page': paginator.page.number,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'data': serializer.data,
    }
    return Response(data_response)

@api_view(['GET'])
def itemsCheckOut(request, pk):
    items = models.OrderContainer.objects.filter(customer=pk)
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(items, request)
    serializer = serializers.ItemsCheckOutSerializer(result_page, many=True)
    data_response = {
        'status': "success",
        'total_data': paginator.page.paginator.count,
        'total_pages': paginator.page.paginator.num_pages,
        'current_page': paginator.page.number,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'data': serializer.data,
    }
    return Response(data_response)