from django.urls import path
from .views import SignupView, LogoutView

urlpatterns = [
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]
