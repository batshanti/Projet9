
from django.shortcuts import render
from django.views.generic import View
from LITReview.forms import SignupForm, LoginForm 

# class Index(View):
#     template_name = 'index.html'
#     form_class = LoginForm

#     def get(self, request):
#         form = self.form_class
#         return render(request, self.template_name, context={'form': form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#         message = 'Identifiants invalides.'
#         return render(request, self.template_name, context={'form': form, 'message' : message})


class Create_User(View):
    template_name = 'CreateUser.html'
    form_class = SignupForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            message = "yes"
        else:
            message = "Invalide"
            
        return render(request, self.template_name, context={'form': form, 'message': message})