from django.urls import path
from . import views

urlpatterns = [ 
    path('api/', views.customers),
    path('api/check-out/<int:pk>/', views.itemsCheckOut),
]
