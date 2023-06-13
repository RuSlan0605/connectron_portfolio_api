from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from app.models import Project, Staff, Field
from api.serializers import ProjectSerializer
from api.serializers import StaffSerializer
from api.serializers import FieldSerializer

class ListPagination(PageNumberPagination):

    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 500

class ProjectViewset(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ListPagination

class StaffListAPIView(generics.ListCreateAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = ListPagination

class StaffAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = ListPagination

class FieldListAPIView(generics.ListCreateAPIView):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    pagination_class = ListPagination

class FieldAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    pagination_class = ListPagination

