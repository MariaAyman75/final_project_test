# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import MenuItem
# from .serializers import MenuItemSerializer
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend

# # Create your views here.

# class MenuItemViewSet(viewsets.ModelViewSet):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['category', 'country']
#     search_fields = ['name', 'description']

#     # def get_queryset(self):
#     #     queryset = MenuItem.objects.all()
#     #     category = self.request.query_params.get('category')
#     #     country = self.request.query_params.get('country')

#     #     if category:
#     #         queryset = queryset.filter(category=category)

       

#     # def get_queryset(self):
#     #     category = self.request.query_params.get('category')
#     #     if category:
#     #         return MenuItem.objects.filter(category=category)
#     #     return super().get_queryset()
# views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import MenuItem
# from .serializers import MenuItemSerializer

# @api_view(['GET'])
# def menu_items(request):
#     category = request.GET.get('category', None)
#     country = request.GET.get('country', None)

#     # Start with all menu items
#     menu_items = MenuItem.objects.all()

#     # Filter by category if provided
#     if category:
#         menu_items = menu_items.filter(category=category)

#     # Filter by country if provided
#     if country:
#         menu_items = menu_items.filter(country=country)

#     serializer = MenuItemSerializer(menu_items, many=True)
#     return Response(serializer.data)
from rest_framework import viewsets, filters
from .models import MenuItem
from .serializers import MenuItemSerializer
from django_filters.rest_framework import DjangoFilterBackend

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['category', 'country']  # Add filters for category and country
    # search_fields = ['name', 'description']  # Add search functionality for name and description
