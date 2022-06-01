from Review_Ticket.models import UserFollows, Ticket, Review
from django.contrib.auth.models import User

class Database:

    def __init__(self, name=""):
        self.name = name
        self.user = User.objects.get(username=self.name)

    def get_user_follow(self, name):
        pass


    def create_review_ticket(self, form_ticket, form_review):
        ticket = form_ticket.save(commit=False)
        ticket.user = self.user
        ticket.save()
        review = form_review.save(commit=False)
        review.ticket = ticket
        review.headline = ticket.title
        review.user = self.user
        review.save()
