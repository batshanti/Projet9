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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from LITReview.views import CreateUserView
from Review_Ticket.views import Flux, AbonnementsView, CreateTicketView, CreateReviewView, PostsView, UpdateTicketView, DeleteTicketView, DeleteUserFollowsView, CreateReviewFromTicketView

urlpatterns = [
    path('admin/', admin.site.urls, name='adminn'),

    path('', LoginView.as_view(
        template_name='index.html',
        redirect_authenticated_user=True
        ), name='login'),
    path('create_user/', CreateUserView.as_view(), name='create'),
    path('flux/', Flux.as_view(), name='flux'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('logout/', LogoutView.as_view(
        template_name='logout.html'
        ), name='logout'),
    path('abonnements/', AbonnementsView.as_view(), name='abonnements'),
    path('create_ticket/', login_required(CreateTicketView.as_view(), login_url='login'), name='create_ticket'),
    path('create_review/', CreateReviewView.as_view(), name='create_review'),
    path('edit_ticket/<int:pk>/', UpdateTicketView.as_view(), name='edit_ticket'),
    path('delete_ticket/<int:pk>/', DeleteTicketView.as_view(), name='delete_ticket'),
    path('delete_followed_user/<int:pk>/', DeleteUserFollowsView.as_view(), name='delete_followed_user'),
    path('review_ticket/<int:pk>/', CreateReviewFromTicketView.as_view(), name='review_ticket'),

]

# test
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)