from django import forms

class Folow_User(forms.Form):

    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
