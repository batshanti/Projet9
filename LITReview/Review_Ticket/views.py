from django.shortcuts import render, reverse, redirect
from django.views.generic import View, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Review_Ticket.forms import FolowUserForm, CreateTicketForm
from Review_Ticket.forms import CreateReviewForm, CreateReviewTicketForm
from Review_Ticket.models import UserFollows, Ticket, Review
from Review_Ticket.utils import create_review_ticket, get_user_follow
from Review_Ticket.utils import get_ticket_user_follow, get_ticket
from Review_Ticket.utils import create_review_from_ticket


class Flux(View):
    template_name = 'flux.html'

    def get(self, request):
        user_log = request.user.get_username()
        user_follow = get_user_follow(user_log)
        ticket_user_follow = get_ticket_user_follow(user_follow, user_log)

        return render(
            request,
            self.template_name,
            context={
                    'user_log': user_log,
                    'ticket_user_follow': ticket_user_follow
                }
        )


class PostsView(View):
    template_name = "Posts.html"

    def get(self, request):
        user_log = request.user.get_username()
        user_bdd = User.objects.get(username=user_log)
        tickets = Ticket.objects.filter(user=user_bdd)

        return render(
            request,
            self.template_name,
            context={'tickets': tickets, 'user_log': user_log}
            )


class AbonnementsView(View):
    template_name = 'abonnements.html'
    form_class = FolowUserForm

    def get(self, request):
        form = self.form_class()
        user_log = request.user.get_username()
        fl_user = UserFollows.get_user_follow(user_log)
        followers = UserFollows.get_followers(user_log)

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
        form_review = self.form_class(request.POST)
        if form_ticket.is_valid() and form_review.is_valid():

            create_review_ticket(user_log, form_ticket, form_review)

        return render(request, self.template_name)


class CreateReviewFromTicketView(View):
    template_name = 'create_review_from_ticket.html'
    form_class = CreateReviewTicketForm

    def get(self, request, pk):
        ticket = get_ticket(pk)
        form = self.form_class({'headline': ticket.title})
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

        return render(request, self.template_name)


class UpdateTicketView(UpdateView):
    model = Ticket
    template_name = 'create_ticket.html'
    form_class = CreateTicketForm

    def get_success_url(self):
        return reverse('posts')


class DeleteTicketView(DeleteView):
    model = Ticket
    template_name = 'delete_ticket.html'

    def get_success_url(self):
        return reverse('posts')


class DeleteUserFollowsView(DeleteView):
    model = UserFollows
    template_name = 'delete_userfollows.html'

    def get_success_url(self):
        return reverse('abonnements')