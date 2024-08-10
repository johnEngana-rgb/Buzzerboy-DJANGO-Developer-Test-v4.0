from django.contrib.auth import views as auth_views
from django.urls import path
from .forms import EmailAuthenticationForm
from .views import CustomLoginView, CustomLogoutView, CustomPasswordChangeView, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetView, profile_view, select_profile, switch_profile, signup
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('change-password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('change-password-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('switch_profile/<int:profile_id>/', switch_profile, name='switch_profile'),
    path('signup/', signup, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('select_profile/', select_profile, name='select_profile'),  # Add this line
]
