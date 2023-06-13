from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectViewset
from .views import StaffListAPIView
from .views import FieldListAPIView
from .views import StaffAPIView
from .views import FieldAPIView

router = SimpleRouter()
router.register('', ProjectViewset, basename='projects')

urlpatterns = [
    path('staffs/', StaffListAPIView.as_view(), name='staffs'),
    path('staffs/<int:pk>/', StaffAPIView.as_view(), name='staff'),
    path('field/', FieldListAPIView.as_view(), name='fields'),
    path('field/<int:pk>/', FieldAPIView.as_view(), name='field'),
]
urlpatterns += router.urls