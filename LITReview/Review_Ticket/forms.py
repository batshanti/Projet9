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
        choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")),
        label='Note'
    )

    class Meta:
        model = Review
        fields = ('rating', 'body')
        labels = {

            'rating': 'Note',
            'body': 'Commentaire',
        }

class CreateReviewTicketForm(forms.ModelForm):
    rating = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")),
        label='Note'
    )

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        labels = {

            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
        widgets = {

            'body': forms.Textarea,
        }