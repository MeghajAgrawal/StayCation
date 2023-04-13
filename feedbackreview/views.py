from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from feedbackreview.models import Feedback
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class Feedbacklistview(ListView):
    model=Feedback
    template_name='feedback/feedback.html'
    context_object_name='feedbacks'

class FeedbackDetailView(DetailView):
    model=Feedback
    template_name='feedback/feedback_detail.html'

class FeedbackCreateView(CreateView):
    model=Feedback
    fields=['title','content']
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    template_name='feedback/feedback_create.html'
    
class FeedbackDeleteView(DeleteView):
    model=Feedback
    def test_func(self):
        feedback=self.get_object()
        if self.request.user==feedback.user:
            return True
        return False
    template_name='feedback/feedback_delete.html'
    success_url='/'

class FeedbackUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Feedback
    fields=['title','content']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def test_func(self):
        feedback=self.get_object()
        if self.request.user==feedback.user:
            return True
        return False
    template_name='feedback/feedback_update.html'

