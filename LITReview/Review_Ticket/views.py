from itertools import chain
from django.shortcuts import render, reverse, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db.models import CharField, Value
from Review_Ticket.forms import FolowUserForm, CreateTicketForm
from Review_Ticket.forms import CreateReviewForm
from Review_Ticket.models import UserFollows, Ticket, Review
from Review_Ticket.utils import (
    create_review_ticket,
    get_user_follow,
    get_ticket_user_follow,
    get_ticket,
    create_review_from_ticket,
    get_review_user_follow,
    get_followers
)


class Flux(View):
    """Class-based views used to display user flux

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'flux.html'

    def get(self, request):
        user_log = request.user.get_username()
        user_follow = get_user_follow(user_log)
        tickets = get_ticket_user_follow(user_follow, user_log)
        reviews = get_review_user_follow(user_follow, user_log)

        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        stars = [0, 1, 2, 3, 4, 5]
        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )

        return render(
            request,
            self.template_name,
            context={
                'posts': posts,
                'user_log': user_log,
                'stars': stars
            }
        )


class PostsView(View):
    """Class-based views used to display user posts

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = "Posts.html"

    def get(self, request):
        user_log = request.user.get_username()
        user_bdd = User.objects.get(username=user_log)
        tickets = Ticket.objects.filter(user=user_bdd)
        print(tickets)
        reviews = Review.objects.filter(user=user_bdd)

        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )

        return render(
            request,
            self.template_name,
            context={
                'posts': posts,
                'user_log': user_log,
            }
        )


class AbonnementsView(View):
    """Class-based views used to manage followers

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'abonnements.html'
    form_class = FolowUserForm

    def get(self, request):
        form = self.form_class()
        user_log = request.user.get_username()
        fl_user = get_user_follow(user_log)
        followers = get_followers(user_log)

        return render(
            request,
            self.template_name,
            context={'form': form,
                     'user_log': user_log,
                     'fl_user': fl_user,
                     'followers': followers}
        )

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            usr_log = request.user.get_username()
            user_search = form.cleaned_data['username']
            user_bdd = User.objects.get(username=user_search)
            user_log_bdd = User.objects.get(username=usr_log)

            fl_user = UserFollows.objects.create(
                user=user_log_bdd,
                followed_user=user_bdd,
            )
            fl_user.save()

        return self.get(request)


class CreateTicketView(View):
    """Class-based views used to Create ticket

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'create_ticket.html'
    form_class = CreateTicketForm

    def get(self, request):
        form = self.form_class()
        user_log = request.user.get_username()

        return render(
            request,
            self.template_name,
            context={'form': form, 'user_log': user_log}
        )

    def post(self, request):
        user_log = request.user.get_username()
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            user_bdd = User.objects.get(username=user_log)
            ticket = form.save(commit=False)
            ticket.user = user_bdd
            ticket.save()
            form = self.form_class()
            message = "Ajout demande de critique ok"

        return render(
            request,
            self.template_name,
            context={'form': form, 'user_log': user_log, 'message': message}
        )


class CreateReviewView(View):
    """Class-based views used to create review

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'create_review.html'
    form_class = CreateReviewForm

    def get(self, request):
        form1 = CreateTicketForm()
        form2 = self.form_class()
        user_log = request.user.get_username()

        return render(
            request,
            self.template_name,
            context={'form1': form1, 'form2': form2, 'user_log': user_log}
        )

    def post(self, request):
        user_log = request.user.get_username()
        form_ticket = CreateTicketForm(request.POST, request.FILES)
        print(type(form_ticket))
        form_review = self.form_class(request.POST)
        if form_ticket.is_valid() and form_review.is_valid():
            create_review_ticket(user_log, form_ticket, form_review)

        return self.get(request)


class CreateReviewFromTicketView(View):
    """Class-based views used to create review from existing ticket

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'create_review_from_ticket.html'
    form_class = CreateReviewForm

    def get(self, request, pk):
        ticket = get_ticket(pk)
        form = self.form_class()
        user_log = request.user.get_username()
        return render(
            request,
            self.template_name,
            context={'form': form, 'user_log': user_log, 'ticket': ticket}
        )

    def post(self, request, pk):
        ticket = get_ticket(pk)
        form_review = self.form_class(request.POST)
        user_log = request.user.get_username()
        if form_review.is_valid():

            create_review_from_ticket(user_log, form_review, ticket)

        return redirect('flux')


class UpdateTicketView(UpdateView):
    """class-based generic views (Update)

    Attributes:
        form_class : Class name used to create form
        model : Model class name
        template_name (str): html file name for template
    """
    model = Ticket
    template_name = 'create_ticket.html'
    form_class = CreateTicketForm

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            user=self.request.user
        )

    def get_success_url(self):
        return reverse('posts')


class DeleteTicketView(DeleteView):
    """class-based generic views (Delete)

    Attributes:
        model : Model class name
        template_name (str): html file name for template
    """
    model = Ticket
    template_name = 'delete_ticket.html'

    def get_success_url(self):
        return reverse('posts')


class DeleteUserFollowsView(DeleteView):
    """class-based generic views (Delete)

    Attributes:
        model : Model class name
        template_name (str): html file name for template
    """
    model = UserFollows
    template_name = 'delete_userfollows.html'

    def get_success_url(self):
        return reverse('abonnements')


class UpdateReviewView(UpdateView):
    """class-based generic views (Update)

    Attributes:
        model : Model class name
        template_name (str): html file name for template
        form_class : Class name used to create form
    """
    model = Review
    template_name = 'update_review.html'
    form_class = CreateReviewForm

    def get_success_url(self):
        return reverse('posts')


class DeleteReviewView(DeleteView):
    """class-based generic views (Delete)

    Attributes:
        model : Model class name
        template_name (str): html file name for template
    """
    model = Review
    template_name = 'delete_review.html'

    def get_success_url(self):
        return reverse('posts')
