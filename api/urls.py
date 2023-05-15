from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProjectViewset
from .views import StaffViewset
from .views import FieldAPIView

router = SimpleRouter()
router.register('', ProjectViewset, basename='projects')
router.register('staffs', StaffViewset, basename='staffs')

urlpatterns = [
    path('field/', FieldAPIView.as_view(), name='fields')
]
urlpatterns += router.urls