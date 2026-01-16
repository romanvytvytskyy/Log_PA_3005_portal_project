from django.urls import path
from .views import SignUpView, UserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]