# django middleware based on (AuthenticationMiddleware(MiddlewareMixin
# (2 methods: process_request + process_reponse)
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

User = get_user_model()

class CheckUserIsBanned(MiddlewareMixin):
    def process_request(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            # user_obj = get_object_or_404(User,user=user)
            if request.user.banned:
                logout(request)
                # re-direct to the home page
                return HttpResponseRedirect('/')




