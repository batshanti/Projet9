from django import forms
from Review_Ticket.models import Ticket, Review


class Folow_User(forms.Form):

    username = forms.CharField(max_length=63, label='Nom d’utilisateur')

class Create_ticket_form(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image',)
        labels = {

            'title': 'Titre'
        }

class Create_review_form(forms.ModelForm):
    rating = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=((1, "1 star"), (2, "2 stars"), (3, "3 stars"), (4, "4 stars"), (5, '5 stars'))
    )

    class Meta:
        model = Review
        fields = ('rating', 'body')
        labels = {

            'rating': 'Note',
            'body': 'Commentaire',
        }