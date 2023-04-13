from django.urls import path
from .views import PlaceListView1,PlaceListView2,PlaceDetailView,PlaceCreateView,PlaceUpdateView,PlaceDeleteView
from . import views
urlpatterns=[
    path('destinations',PlaceListView1.as_view(),name='destinations'),
    path('destinations/<str:dest_city>/',PlaceListView2.as_view(),name='dest_name'),
    path('place/<int:pk>/',PlaceDetailView.as_view(),name='place-detail'),
    path('place/new/',PlaceCreateView.as_view(),name='place-create'),
    path('place/<int:pk>/update',PlaceUpdateView.as_view(),name='place-update'),
    path('place/<int:pk>/delete',PlaceDeleteView.as_view(),name='place-delete'),
    path('search_place',views.search,name='search_place')
]