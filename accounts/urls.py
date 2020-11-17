# accounts/urls.py
from django.urls import path, include
from accounts.views import SignUpView 
from accounts.apis import UserViewSet 
from rest_framework import routers

# Api routes
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
]

