from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('contact/',include('contact.urls')),
    path('about/',include('about.urls')),
    path('destinations/',include('destinations.urls')),
    path('profiles/',include('profiles.urls')),
    path('place/',include('place.urls')),
    path('feedback/',include('feedbackreview.urls')),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
