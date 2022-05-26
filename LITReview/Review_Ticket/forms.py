from django import forms
from Review_Ticket.models import Ticket

class Folow_User(forms.Form):

    username = forms.CharField(max_length=63, label='Nom d’utilisateur')

class Create_ticket(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image',)



