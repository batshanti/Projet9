from django import forms
from Review_Ticket.models import Ticket, Review


class FolowUserForm(forms.Form):

    username = forms.CharField(max_length=63, label='Nom d’utilisateur')

class CreateTicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image',)
        labels = {

            'title': 'Titre'
        }

class CreateReviewForm(forms.ModelForm):
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