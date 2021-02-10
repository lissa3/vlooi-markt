# django middleware based on (AuthenticationMiddleware(MiddlewareMixin
# (2 methods: process_request + process_reponse)
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib import messages
from django.contrib.auth import logout

# https://stackoverflow.com/questions/50265160/how-to-add-banned-users-to-table-and-send-details-to-users-email-within-django
# for more complex relations (banned +> email)
User = get_user_model()


class CheckUserIsBanned(MiddlewareMixin):
    def process_request(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # user_obj = get_object_or_404(User,user=user)
            if request.user.banned:
                try:
                    messages.add_message(request, messages.WARNING, 'This account hab been banned')
                except messages.MessageFailure:
                    pass
                logout(request)
                # re-direct to the home page
                return HttpResponseRedirect('/')
                # return HttpResponseRedirect(settings.LOGIN_URL)
