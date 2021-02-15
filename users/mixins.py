from django.urls import reverse_lazy
from django.views.generic import TemplateView
from braces.views import UserPassesTestMixin


class UserPassesBannedView(UserPassesTestMixin):
    permission_denied_message = "Your account is banned"
    raise_exception = True
    redirect_field_name = reverse_lazy('banned')


    def test_func(self, user):
        print("user is banned", user.banned)
        return not user.banned
        # if user.banned:
        #     raise PermissionError("hghghghg")
        # else:
        #     return True


    def get_permisision_denied_message(self):
        print("msg",self.permission_denied_message)
        # raise PermissionDenied("Custom message")
        return self.permission_denied_message



#
# class SomeUserPassView(UserPassesTestMixin, TemplateView):
#     def test_func(self, user):
#         return (user.is_staff and not user.is_superuser
#                 and user.email.endswith(u"mydomain.com"))
