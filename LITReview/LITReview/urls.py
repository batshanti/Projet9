"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from LITReview.views import Create_User
from Review_Ticket.views import Dashboard, Abonnements, Create_ticket

urlpatterns = [
    path('admin/', admin.site.urls, name='adminn'),

    path('index/', LoginView.as_view(
        template_name='index.html',
        redirect_authenticated_user=True
        ), name='login'),
    path('create_user/', Create_User.as_view(), name='create'),
    path('dashboard/' , Dashboard.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(
        template_name='logout.html'
        ), name='logout'),
    path('abonnements/', Abonnements.as_view(), name='abonnements'),
    path('create_ticket/', Create_ticket.as_view(), name='create_ticket')
]
