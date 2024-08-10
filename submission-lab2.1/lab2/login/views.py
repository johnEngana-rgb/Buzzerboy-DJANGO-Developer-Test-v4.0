from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView
)
from .forms import EmailAuthenticationForm, CustomPasswordResetForm, SignupForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, get_user_model, get_backends
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils import translation
from django.contrib import messages

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
    success_url = reverse_lazy('index')  # Default success URL if no profile selection is needed

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        user_profiles = UserProfile.objects.filter(user=user)

        if user_profiles.count() > 1:
            # If the user has multiple profiles, redirect them to select a profile
            return redirect('select_profile')
        elif user_profiles.exists():
            # If the user has only one profile, set it as active
            user_profile = user_profiles.first()
            self.request.session['active_profile_id'] = user_profile.id
            translation.activate(user_profile.language)
            self.request.session[translation.LANGUAGE_SESSION_KEY] = user_profile.language
        else:
            messages.warning(self.request, "User profile not found. Default language will be used.")

        return super().form_valid(form)

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('password_change_done')

def login_view(request):
    form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def get_active_profile(request):
    profile_id = request.session.get('selected_profile_id')
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
    user_profiles = UserProfile.objects.filter(user=request.user)

    # Try to get the selected profile ID from the session
    selected_profile_id = request.session.get('selected_profile_id')
    if selected_profile_id:
        user_profile = get_object_or_404(UserProfile, id=selected_profile_id, user=request.user)
    else:
        # If no profile is selected, use the first profile as the default
        user_profile = user_profiles.first()
        request.session['selected_profile_id'] = user_profile.id

    return render(request, 'profile.html', {
        'user_profiles': user_profiles,
        'user_profile': user_profile,
    })

@login_required
def select_profile(request):
    user_profiles = UserProfile.objects.filter(user=request.user)

    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        user_profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
        request.session['selected_profile_id'] = user_profile.id
        translation.activate(user_profile.language)
        request.session['django_language'] = user_profile.language
        return redirect('index')  # Redirect to the home page or any other view

    return render(request, 'select_profile.html', {'user_profiles': user_profiles})


    
@login_required
def switch_profile(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    if profile.user == request.user:
        request.session['selected_profile_id'] = profile.id
        translation.activate(profile.language)
        request.session['django_language'] = profile.language

    # Redirect to the profile view to reflect the selected profile
    return redirect(request.META.get('HTTP_REFERER', 'index'))
