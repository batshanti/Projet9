from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Review_Ticket.forms import Folow_User, Create_ticket, Create_Review
from Review_Ticket.models import UserFollows, Ticket, Review
from Review_Ticket.utils import Database



class Flux(View):
    template_name = 'flux.html'

    def get(self, request):
        user_log = request.user.get_username()
        data = Database(user_log)

        return render(request, self.template_name,context={'user_log': user_log})


class Posts(View):
    pass

class Abonnements(View):
    template_name = 'abonnements.html'
    form_class = Folow_User
    
    def get(self, request):
        form = self.form_class()
        user_log = request.user.get_username()
        fl_user = UserFollows.get_user_follow(user_log)
        followers = UserFollows.get_followers(user_log)

        return render(request, self.template_name, context={'form': form,
                                                            'user_log': user_log,
                                                            'fl_user': fl_user,
                                                            'followers': followers})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            usr_log = request.user.get_username()
            user_search = form.cleaned_data['username']
            user_bdd = User.objects.get(username=user_search)
            user_log_bdd = User.objects.get(username=usr_log)

            fl_user = UserFollows.objects.create(user=user_log_bdd, followed_user=user_bdd)
            fl_user.save()

        return render(request, self.template_name)


class Create_ticket(View):
    template_name = 'create_ticket.html'
    form_class = Create_ticket
    # redirect_field_name = '/'
    

    def get(self, request):
        form = self.form_class()
        user_log = request.user.get_username()

        return render(request, self.template_name, context={'form': form, 'user_log': user_log})

    def post(self, request):
        user_log = request.user.get_username()
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user_bdd = User.objects.get(username=user_log)
            ticket = form.save(commit=False)
            ticket.user = user_bdd
            ticket.save()

        return render(request, self.template_name)

class Create_Review_View(View):
    template_name = 'create_review.html'
    form_class = Create_Review
    

    def get(self, request):
        form1 = Create_ticket.form_class()
        form2 = self.form_class()
        user_log = request.user.get_username()

        return render(request, self.template_name, context={'form1': form1, 'form2': form2, 'user_log': user_log})

    def post(self, request):
        pass
        
        
