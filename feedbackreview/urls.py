from django.urls import path
from .views import FeedbackCreateView,FeedbackDetailView,Feedbacklistview,FeedbackDeleteView,FeedbackUpdateView
from . import views
urlpatterns=[
    path('feedback',Feedbacklistview.as_view(),name='feedbacks'),
    path('feedback/<int:pk>',FeedbackDetailView.as_view(),name='feedback-detail'),
    path('feedback/<int:pk>/delete',FeedbackDeleteView.as_view(),name='feedback-delete'),
    path('feedback/<int:pk>/update',FeedbackUpdateView.as_view(),name='feedback-update'),
    path('feedback/new/',FeedbackCreateView.as_view(),name='feedback-create'),

]