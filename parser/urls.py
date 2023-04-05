from django.urls import path
from . import views

urlpatterns = [
    path('laptop_list/', views.ParserLaptopView.as_view(), name='laptop_list'),
    path('parser_laptop/', views.ParserFormView.as_view(), name='start_parsing'),
]