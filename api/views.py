from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from app.models import Project, Staff, Field
from api.serializers import ProjectSerializer
from api.serializers import StaffSerializer
from api.serializers import FieldSerializer
from .permissions import IsOwnerOrReadOnly

class ListPagination(PageNumberPagination):

    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 500

class ProjectViewset(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ListPagination
    permission_classes = (IsOwnerOrReadOnly, )

class StaffViewset(viewsets.ModelViewSet):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = ListPagination
    permission_classes = (IsOwnerOrReadOnly, )

class FieldAPIView(generics.ListCreateAPIView):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    pagination_class = ListPagination
    permission_classes = (IsOwnerOrReadOnly, )
