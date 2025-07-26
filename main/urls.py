from django.urls import path
from .views import home, group_detail, CustomLoginView


urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('davomat/<int:pk>', group_detail, name='group_detail'),
]
