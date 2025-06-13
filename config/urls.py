from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views  # Importa las vistas de accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URLs de autenticación
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
        path('signup/', accounts_views.signup, name='signup'),  # Añade esta línea
        path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
        path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
        path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
        path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
        path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    ])),
    
    # URLs de aplicaciones
    path('issues/', include('issues.urls', namespace='issues')),
    path('', include('pages.urls')),
]