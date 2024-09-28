from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet

router = DefaultRouter()

router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/bookings/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]