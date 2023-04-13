from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from place.models import Place,Booking,Review
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
class PlaceListView(ListView):
    model=Place
    template_name='my-listing.html'
    context_object_name='places'
 
class BookingsListView(ListView):
    model=Booking
    template_name='my-bookings.html'
    context_object_name='booking'
    ordering=['place']
    
class BookingsDetailView(DetailView):
    model=Booking
    template_name='booking/booking_detail.html'

class BookingsCreateView(LoginRequiredMixin,CreateView):
    model=Booking
    fields=['checkin','checkout']
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        form.instance.place=get_object_or_404(Place,title=self.kwargs.get('place'))
        return super().form_valid(form)
    template_name='booking/book.html'
    
class BookingsDeleteView(DeleteView):
    model=Booking
    def test_func(self):
        book=self.get_object()
        if self.request.user==book.user:
            return True
        return False
    template_name='booking/booking_cancel.html'
    success_url='/'


class ReviewListView(ListView):
    model=Review
    template_name='review/review.html'
    context_object_name='review'
    
class ReviewDetailView(DetailView):
    model=Review
    template_name='review/review_detail.html'

class ReviewCreateView(LoginRequiredMixin,CreateView):
    model=Review
    fields=['title_review','stars','content']
    
    def form_valid(self,form):
        form.instance.user_review=self.request.user
        form.instance.place_review=get_object_or_404(Place,title=self.kwargs.get('place'))
        return super().form_valid(form)
        
    template_name='review/review_create.html'
    
class ReviewDeleteView(DeleteView):
    model=Review
    def test_func(self):
        review=self.get_object()
        if self.request.user==review.user_review:
            return True
        return False
    template_name='review/review_delete.html'
    success_url='/'

class ReviewUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Review
    fields=['title_review','stars','content']
    def form_valid(self,form):
        form.instance.user_review=self.request.user
        return super().form_valid(form)
    def test_func(self):
        review=self.get_object()
        if self.request.user==review.user_review:
            return True
        return False
    template_name='review/review_update.html'