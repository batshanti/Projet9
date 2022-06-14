from itertools import chain
from Review_Ticket.models import UserFollows, Ticket, Review
from django.contrib.auth.models import User
from django.db.models import CharField, Value

def get_ticket(pk):
    ticket = Ticket.objects.get(pk=pk)
    return ticket


def get_user_follow(user_log):
    user_bdd = User.objects.get(username=user_log)
    return UserFollows.objects.filter(user=user_bdd)


def create_review_ticket(name, form_ticket, form_review):
    ticket = form_ticket.save(commit=False)
    ticket.user = User.objects.get(username=name)
    ticket.save()
    review = form_review.save(commit=False)
    review.ticket = ticket
    review.user = User.objects.get(username=name)
    review.save()


def get_ticket_user_follow(user_follow, user_log):
    users_follow = []
    for user in user_follow:
        users_follow.append(user.followed_user.id)

    user_bdd = User.objects.get(username=user_log)
    tickets = Ticket.objects.filter(user__in=users_follow) | Ticket.objects.filter(user=user_bdd)
    
    return tickets


def get_review_user_follow(user_follow, user_log):
    users_follow = []
    for user in user_follow:
        users_follow.append(user.followed_user.id)

    user_bdd = User.objects.get(username=user_log)    
    reviews = Review.objects.filter(user__in=users_follow) | Review.objects.filter(user=user_bdd)

    return reviews


def create_review_from_ticket(user_log, form_review, ticket):
    review = form_review.save(commit=False)
    review.ticket = ticket
    review.user = User.objects.get(username=user_log)
    review.save()

