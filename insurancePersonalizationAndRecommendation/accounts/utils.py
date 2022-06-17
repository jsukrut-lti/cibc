from .models import CustomUser
# return user obj
def get_user_obj(user):
    if user:
        queryset = CustomUser.objects.filter(id = user.id)
        usr_obj = queryset[0]
        return usr_obj
