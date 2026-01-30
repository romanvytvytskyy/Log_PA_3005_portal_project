from django.urls import path
from .views import ThreadListView, ThreadDetailView, PostCreateView, ThreadCreateView


urlpatterns = [
    path('', ThreadListView.as_view(), name='thread_list'),
    path('new/', ThreadCreateView.as_view(), name='thread_create'),
    path('<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('<int:pk>/create/', PostCreateView.as_view(), name='post_create'),
]
