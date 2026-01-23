from django.urls import path
from .views import SignupView, LogoutView, CreateAdminView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('create-admin/', CreateAdminView.as_view()),  # TEMP
]
