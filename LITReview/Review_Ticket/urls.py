from django.urls import path
from django.contrib.auth.decorators import login_required
from Review_Ticket.views import Flux, AbonnementsView, CreateTicketView, CreateReviewView, PostsView, UpdateTicketView, DeleteTicketView, DeleteUserFollowsView, CreateReviewFromTicketView, UpdateReviewView, DeleteReviewView

urlpatterns = [
    path(
        'flux/',
        login_required(Flux.as_view(),login_url='login'),
        name='flux'
    ),
    path(
        'posts/',
        login_required(PostsView.as_view(), login_url='login'),
        name='posts'
    ),
    path(
        'abonnements/',
        login_required(AbonnementsView.as_view(), login_url='login'),
        name='abonnements'
    ),
    path(
        'create_ticket/',
        login_required(CreateTicketView.as_view(), login_url='login'),
        name='create_ticket'
    ),
    path(
        'create_review/',
        login_required(CreateReviewView.as_view(), login_url='login'),
        name='create_review'
    ),
    path(
        'edit_ticket/<int:pk>/',
        login_required(UpdateTicketView.as_view(), login_url='login'),
        name='edit_ticket'
    ),
    path(
        'delete_ticket/<int:pk>/',
        login_required(DeleteTicketView.as_view(), login_url='login'),
        name='delete_ticket'
    ),
    path(
        'delete_followed_user/<int:pk>/',
        login_required(DeleteUserFollowsView.as_view(), login_url='login'),
        name='delete_followed_user'
    ),
    path(
        'review_ticket/<int:pk>/',
        login_required(CreateReviewFromTicketView.as_view(), login_url='login'),
        name='review_ticket'
    ),
    path(
        'edit_review/<int:pk>/',
        login_required(UpdateReviewView.as_view(), login_url='login'),
        name='edit_review'
    ),
    path(
        'delete_review/<int:pk>/',
        login_required(DeleteReviewView.as_view(), login_url='login'),
        name='delete_review'
    )
]