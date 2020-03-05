from django.urls import path
from lab_1.views import LoginView


urlpatterns = [
    path('', LoginView.as_view())
]