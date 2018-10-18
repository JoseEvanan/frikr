from django.contrib.auth import authenticate, login as django_login, \
    logout as django_logout
from django.shortcuts import redirect, render

from users.forms import LoginForm


# Create your views here.
def login(request):
    """
    Login user
    """
    error_messages = []
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            #username = request.POST.get('usr', '')
            #password = request.POST.get('pwd', '')
            user = authenticate(username=username, password=password)
            if not user:
                error_messages.append('Nombre de usuario o contraseña incorrecta')
            else:
                if user.is_active:
                    django_login(request, user)
                    url =  request.GET.get('next', 'photos_home')
                    return redirect(url)
                else:
                    error_messages.append(
                        'Usuario no activo')
    else:
        form = LoginForm()
    context = {
        'errors': error_messages,
        'login_form': form
    }
    
    return render(request, 'users/login.html', context)

def logout(request):
    """
    Logout user
    """
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('photos_home')
    
