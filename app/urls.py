from django.urls import path
from .views import WheelSpecificationView

urlpatterns = [
    path('forms/wheel-specifications', WheelSpecificationView.as_view()),
]
