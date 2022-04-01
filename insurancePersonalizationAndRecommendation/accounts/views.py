from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

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