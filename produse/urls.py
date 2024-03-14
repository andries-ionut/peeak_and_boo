from django.urls import path
from .views import Produseview

urlpatterns = [
    path('', Produseview.as_view()),]