from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .utils import get_user_obj
from django.shortcuts import redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            form = AuthenticationForm()
            render(request, 'login.html', {'form': form})
    else:
        # Return an 'invalid login' error message.
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



def home(request):
    if request:
        print("-----------------")
        usr_obj = get_user_obj(request.user)
        user_groups = usr_obj.groups.values_list('name', flat=True)
        if 'ADVISOR' in user_groups:
            print("--ADVISOR")
            response = redirect("/insurance/ci_pre_application")
            return response
        elif 'CIBCADMIN' or 'CIBCSUPERVISOR' in user_groups:
            response = redirect('/admin/')
            print("--dsfsjk")
            return response
        else:
            ''' crearte new user/ assign roles to new user '''
            pass



