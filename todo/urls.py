from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TasksViewSet, UserViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]