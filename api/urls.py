from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectViewset
from .views import StaffAPIView
from .views import FieldAPIView

router = SimpleRouter()
router.register('', ProjectViewset, basename='projects')

urlpatterns = [
    path('staffs/', StaffAPIView.as_view(), name='staffs'),
    path('field/', FieldAPIView.as_view(), name='fields'),
]
urlpatterns += router.urls