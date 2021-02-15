# Why: to add extra fields to the signup form
from allauth.account.forms import SignupForm
from django import forms

# let op: you need to + settings.py
#ACCOUNT_FORMS = {'signup': 'users.forms.CustomSignupForm'}

class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=16,label='phone') #,widget=())
    def signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.save()
        return user # user will be passed for validation