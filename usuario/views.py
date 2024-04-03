from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 


# Create your views here.
@login_required(login_url='login_register')


def home(request):
    return render(request, 'home.html')




def login_register_view(request):
    if request.method == 'POST':
        if 'login_submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Almacena el nombre de usuario en la sesión
                request.session['username'] = user.username
                return redirect('home')  # Cambia 'home' por la URL de la página a la que deseas redirigir después del inicio de sesión exitoso
            else:
                messages.error(request, 'Los datos de inicio de sesión no son válidos')
        
        elif 'register_submit' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            
            if password1 != password2:
                messages.error(request, 'Las contraseñas no coinciden')
            else:
                try:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    login(request, user)
                    return redirect('login_register')  # Cambia 'login_register' por la URL de la página a la que deseas redirigir después del registro exitoso
                except:
                    messages.error(request, 'Error al registrar el usuario')

    # Obtén el nombre de usuario si está presente en la sesión
    username = request.session.get('username', '')

    return render(request, 'inicioSesion.html', {'username': username})



def LogoutPage(request):
    logout(request)
    return redirect('login_register')


from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

