"""b3_c2_django_serrano_amar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('<int:ecole_id>/reservation/', views.reservation, name='reservation'),
    path('<int:ecole_id>/', views.ecole, name='ecole'),
    path('reservation/<int:reservation_id>/annulation/', views.annulation_reservation, name='annulation_reservation'),
    path('liste_reservations/', views.liste_reservations, name='liste_reservations'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('inscription/', views.inscription, name='inscription'),
]
