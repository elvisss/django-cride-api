"""Users urls"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import users as users_views

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
