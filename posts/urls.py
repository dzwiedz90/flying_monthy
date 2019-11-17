from django.urls import path

from django.urls import path

from .views import List

urlpatterns = [
    path('', List.as_view(), name='home'),
]