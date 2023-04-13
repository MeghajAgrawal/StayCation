from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import UserCreationForm
from place.models import Place
from home.models import Destination
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class PlaceListView1(ListView):
    model=Place
    template_name='destinations.html'
    context_object_name='places'
    ordering=['des_city']
    paginate_by= 9

class PlaceListView2(ListView):
    model=Place
    template_name='destinations.html'
    context_object_name='places'
    paginate_by= 6
    def get_queryset(self):
        place=get_object_or_404(Destination,name=self.kwargs.get('dest_city'))
        return Place.objects.filter(des_city= place).order_by('price')

class PlaceDetailView(DetailView):
    model=Place
    template_name='place_content/place_detail.html'


class PlaceCreateView(LoginRequiredMixin,CreateView):
    model=Place
    fields=['title','address','img','price','rooms','max_occupancy','des_city','offer']

    def form_valid(self,form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)

    template_name='place_content/place_form.html'

class PlaceUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Place
    fields=['title','address','img','price','rooms','max_occupancy','des_city','offer']
    def form_valid(self,form):
        form.instance.posted_by=self.request.user
        return super().form_valid(form)
    def test_func(self):
        place=self.get_object()
        if self.request.user==place.posted_by:
            return True
        return False
    template_name='place_content/place_update.html'

class PlaceDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Place
    def test_func(self):
        place=self.get_object()
        if self.request.user==place.posted_by:
            return True
        return False
    template_name='place_content/place_confirm.html'
    success_url='/'

def search(request):
    if request.method=='GET':
        search_method=request.GET['search_by']
        place_name=request.GET['placename']
        price_value=request.GET['price']
        if(search_method=='Name' and place_name != ''):
                places = Place.objects.filter(title__icontains=place_name)
        elif(search_method=='Addr' and place_name != ''):
                places = Place.objects.filter(address__icontains=place_name)
        elif(int(price_value)!=0):
                places=Place.objects.filter(price__lte=int(price_value))
        else:
            places=Place.objects.all()
        context={'places':places,}
        return render(request,'destinations.html',context)
