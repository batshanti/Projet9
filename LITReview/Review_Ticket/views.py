from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from Review_Ticket.forms import Folow_User
from Review_Ticket.models import UserFollows



class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class Flux(View):
    pass

class Posts(View):
    pass

class Abonnements(View):
    template_name = 'abonnements.html'
    form_class = Folow_User
    
    def get(self, request):
        form = self.form_class()

        usr_log = request.user.get_username()
        user_log_bdd = User.objects.get(username=usr_log)
        
        fl_user = UserFollows.objects.filter(user=user_log_bdd)

        return render(request, self.template_name, context={'form': form, 'fl_user': fl_user})

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


