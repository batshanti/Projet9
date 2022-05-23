from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from Review_Ticket.forms import Folow_User



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
        usr_log = request.user.get_username()
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            user_bdd = User.objects.get(username=user)

        return render(request, self.template_name)


