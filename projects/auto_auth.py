from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

# Created a fake user for a quick django admin setup

class User:
    is_superuser = True
    is_active = True
    is_staff = True
    pk = 1


def return_true(*args, **kwargs):
    return True


User.has_module_perms = return_true
User.has_perm = return_true


class AutoAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = User()