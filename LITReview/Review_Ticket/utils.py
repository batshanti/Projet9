from Review_Ticket.models import UserFollows, Ticket, Review
from django.contrib.auth.models import User

# class Database:

#     def __init__(self, name=""):
#         self.name = name
#         self.user = User.objects.get(username=self.name)

#     def get_user_follow(self, name):
#         pass

#     def create_review_ticket(self, form_ticket, form_review):
#         ticket = form_ticket.save(commit=False)
#         ticket.user = self.user
#         ticket.save()
#         review = form_review.save(commit=False)
#         review.ticket = ticket
#         review.headline = ticket.title
#         review.user = self.user
#         review.save()


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
    review.headline = ticket.title
    review.user = User.objects.get(username=name)
    review.save()

def get_ticket_user_follow(user_follow, user_log):
    users_follow = []
    for user in user_follow:
        users_follow.append(user.followed_user)


    tickets_follow = []

    for user in users_follow :
        tickets = Ticket.objects.filter(user=user)
        for ticket in tickets:
            tickets_follow.append(ticket)
    user_bdd = User.objects.get(username=user_log)
    tickets_user_log = Ticket.objects.filter(user=user_bdd)

    for ticket in tickets_user_log:
        tickets_follow.append(ticket)

    return tickets_follow
