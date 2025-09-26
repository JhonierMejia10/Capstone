from django.urls import path
from . import views
from . import views


urlpatterns = [
    path('menu', views.menuview.as_view()),
    path('booking', views.bookingview.as_view()),
    
]   