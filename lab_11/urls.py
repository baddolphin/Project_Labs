from django.urls import path
from lab_11.views import LoginView


urlpatterns = [
    path('', LoginView.as_view())
]