
from django.shortcuts import render, redirect
from django.views.generic import View
from LITReview.forms import SignupForm


class CreateUserView(View):
    """Class-based views used to create User

    Attributes:
        form_class : Class name used to create form
        template_name (str): html file name for template
    """
    template_name = 'CreateUser.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            message = "Invalide"

        return render(
            request,
            self.template_name,
            context={'form': form, 'message': message}
        )
