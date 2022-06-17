
from django.shortcuts import render, redirect
from django.views.generic import View
from LITReview.forms import SignupForm, LoginForm


class CreateUserView(View):
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
