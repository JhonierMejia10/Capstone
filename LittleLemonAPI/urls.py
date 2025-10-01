from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('api-token-auth/',obtain_auth_token),
    path('booking', include(router.urls)),
    path('menu-items/<int:pk>',views.SingleMenuItem.as_view()),
    
]   


#path('menu', views.menuview.as_view()),
    #path('message/', views.msg)
