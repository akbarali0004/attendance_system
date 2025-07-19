from django.urls import path
from .views import home, group_detail


urlpatterns = [
    path('', home, name='home'),
    path('davomat/<int:pk>', group_detail, name='group_detail'),
]
