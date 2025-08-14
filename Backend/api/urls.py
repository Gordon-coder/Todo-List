from api import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('change-password/', views.change_password, name='change_password'),
]
