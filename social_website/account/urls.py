from django.urls import path
from account.views import dashboard, register_user, registerDone, user_login, editForm, user_list, user_detail, user_follow
from django.contrib.auth import views as auth_views

#app_name = 'account'

urlpatterns = [
    
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login_user'),
    path('register', register_user, name='register'),
    path('register-done', registerDone, name='register_done'),
    path('edit-form/', editForm, name='edit'),
    #LOGIN / LOGOUT
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),

    #PASSWORD CHANGE
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    #RESET PASSWORD
    path('password-reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/(<uidb64>)/(<token>)', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # user profiles
    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>', user_detail, name='user_detail'),

]