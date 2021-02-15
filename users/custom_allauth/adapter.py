from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

# let op: settings.py
# ACCOUNT_ADAPTER = 'YourProject.adapter.RestrictEmailAdapter'

class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self,email):
        RestrictedList = ['zoo@mail.com']
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact admin.')
        return email
# generate_unique_username(self, txts, regex=None)