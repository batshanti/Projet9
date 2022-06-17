from Review_Ticket.models import UserFollows, Ticket, Review
from django.contrib.auth.models import User


def get_ticket(pk):
    """Get ticket with primary key

    Args:
        pk int: primary key

    Returns:
        Obj : Ticket
    """
    ticket = Ticket.objects.get(pk=pk)
    return ticket


def get_user_follow(user_log):
    """Get a user's followers

    Args:
        user_log (str): username

    Returns:
        obj QuerySet: UserFollows
    """
    user_bdd = User.objects.get(username=user_log)
    return UserFollows.objects.filter(user=user_bdd)


def create_review_ticket(name, form_ticket, form_review):
    """Create review and ticket

    Args:
        name (str): Username
        form_ticket (obj): form ticket
        form_review (obj): form review
    """
    ticket = form_ticket.save(commit=False)
    ticket.user = User.objects.get(username=name)
    ticket.save()
    review = form_review.save(commit=False)
    review.ticket = ticket
    review.user = User.objects.get(username=name)
    review.save()


def get_ticket_user_follow(user_follow, user_log):
    """Get all follower's tickets

    Args:
        user_follow (obj): QuerySet UserFollows
        user_log (str): username

    Returns:
       obj QuerySet: Tickets
    """
    users_follow = []
    for user in user_follow:
        users_follow.append(user.followed_user.id)

    user_bdd = User.objects.get(username=user_log)
    tickets = Ticket.objects.filter(
        user__in=users_follow) | Ticket.objects.filter(user=user_bdd)

    return tickets


def get_review_user_follow(user_follow, user_log):
    """Get all follower's reviews

    Args:
        user_follow (obj): QuerySet UserFollows
        user_log (str): username

    Returns:
       obj QuerySet: Reviews
    """
    users_follow = []
    for user in user_follow:
        users_follow.append(user.followed_user.id)

    user_bdd = User.objects.get(username=user_log)
    reviews = Review.objects.filter(
        user__in=users_follow) | Review.objects.filter(user=user_bdd)

    return reviews


def create_review_from_ticket(user_log, form_review, ticket):
    """Create review from existing ticket

    Args:
        user_log (str): username
        form_review (obj): review form
        ticket (obj): Ticket
    """
    review = form_review.save(commit=False)
    review.ticket = ticket
    review.user = User.objects.get(username=user_log)
    review.save()
