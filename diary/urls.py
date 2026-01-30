from django.urls import path
from .views import GradeListView, GradeCreateView, GradeUpdateView, GradeDeleteView


urlpatterns = [
    path('', GradeListView.as_view(), name='grade_list'),
    path('add/', GradeCreateView.as_view(), name='grade_create'),
    path('update/<int:pk>/', GradeUpdateView.as_view(), name='grade_update'),
    path('delete/<int:pk>/', GradeDeleteView.as_view(), name='grade_delete'),
]
