
from django import forms


class CreateUserForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
