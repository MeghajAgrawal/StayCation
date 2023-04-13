from django.urls import path
from .views import (
    PlaceListView,
    BookingsListView,
    BookingsCreateView,
    BookingsDeleteView,
    BookingsDetailView,
    ReviewCreateView,
    ReviewDeleteView,
    ReviewListView,
    ReviewDetailView,
    ReviewUpdateView,
    )
from . import views
urlpatterns=[
    path('place',PlaceListView.as_view(),name='my-listing'),

    path('booking',BookingsListView.as_view(),name='my-bookings'),
    path('booking/<int:pk>',BookingsDetailView.as_view(),name='booking-detail'),
    path('booking/<int:pk>/delete',BookingsDeleteView.as_view(),name='book-delete'),
    path('booking/<str:place>',BookingsCreateView.as_view(),name='booking'),

    path('review',ReviewListView.as_view(),name='reviews'),
    path('review/<int:pk>',ReviewDetailView.as_view(),name='review-detail'),
    path('review/<int:pk>/delete',ReviewDeleteView.as_view(),name='review-delete'),
    path('review/<str:place>',ReviewCreateView.as_view(),name='review-create'),
    path('review/<int:pk>/update',ReviewUpdateView.as_view(),name='review-update'),
]