from django.urls import path

from users.views import UserCreateAPIView

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='user-register')
]
