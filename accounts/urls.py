from django.urls import path
from . import views

app_name = 'accounts'  # Esto define el namespace

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # Otras URLs de accounts si las tienes
]