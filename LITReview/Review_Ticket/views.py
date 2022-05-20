from django.shortcuts import render
from django.views.generic import View

class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class Flux(View):
    pass

class Posts(View):
    pass

class Abonnements(View):
    pass
