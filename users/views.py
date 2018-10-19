from django.contrib.auth import authenticate, login as django_login, \
    logout as django_logout
from django.shortcuts import redirect, render
from django.views.generic import View

from users.forms import LoginForm


# Create your views here.

class LoginView(View):
    
    def get(self, request):
        """
        Login user
        """
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Login user
        """
        error_messages = []
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
        
        context = {
            'errors': error_messages,
            'login_form': form
        }
        
        return render(request, 'users/login.html', context)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        """
        Logout user
        """
        if request.user.is_authenticated:
            django_logout(request)
        return redirect('photos_home')


