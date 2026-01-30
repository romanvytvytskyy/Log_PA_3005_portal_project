from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Grade
from django.urls import reverse_lazy
from .forms import GradeForm


# Create your views here.
class GradeListView(LoginRequiredMixin, ListView):
    model = Grade
    template_name = 'diary/grade_list.html'
    context_object_name = 'grades'

    def get_queryset(self):
        if self.request.user.is_staff or self.request.is_moderator:
            return Grade.objects.all()
        return Grade.objects.filter(student=self.request.user)
    
class GradeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Grade
    fields = GradeForm
    template_name = 'diary/grade_form.html'
    success_url = reverse_lazy('grade_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.is_moderator
    
class GradeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grade
    form_valid = GradeForm
    template_name = 'diary/grade_form.html'
    success_url = reverse_lazy('grade_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.is_moderator

#! CRUD
#? C - Create
#? R - Read
#? U - Update
#? D - Delete

class GradeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Grade
    template_name = 'diary/grade_confirm_delete.html'
    success_url = reverse_lazy('grade_list')
    def test_func(self):
        return self.request.user.is_staff or self.request.is_moderator
    