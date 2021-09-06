from django.urls import path
from .views import *
urlpatterns = [
path('', BookAPIView.as_view(), name='home'),

]