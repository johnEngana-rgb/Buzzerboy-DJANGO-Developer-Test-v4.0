from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView
from .forms import EmailAuthenticationForm, CustomPasswordResetForm, SignupForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, get_user_model, get_backends
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'custom_password_reset.html'
    email_template_name = 'password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'custom_password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'custom_password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'custom_password_reset_complete.html'

class CustomLogoutView(LogoutView):
    next_page = 'index'

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')  # Redirect to 'home' or any other page

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')

def login_view(request):
    form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})


def switch_profile(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    if profile.user == request.user:
        request.session['active_profile'] = profile.id
    return redirect('some_view')


def get_active_profile(request):
    profile_id = request.session.get('active_profile')
    if profile_id:
        try:
            return UserProfile.objects.get(id=profile_id, user=request.user)
        except UserProfile.DoesNotExist:
            pass
    # Fallback to a default profile if necessary
    return UserProfile.objects.filter(user=request.user).first()

def debug_login_view(request):
    form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def some_view(request):
    active_profile = get_active_profile(request)
    # Use the active profile for your logic
    return render(request, 'index.html', {'active_profile': active_profile})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Get the first authentication backend (usually you have only one)
            backend = get_backends()[0]
            login(request, user, backend=backend.__class__.__module__ + '.' + backend.__class__.__name__)
            return redirect('login')  # Replace 'index' with your desired redirect after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})



class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')  # Redirect to a success page after password change



@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def switch_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
    request.session['active_profile_id'] = profile.id
    return redirect('profile_detail')  # Redirect to a relevant view