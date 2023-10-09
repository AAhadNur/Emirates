from django.urls import path

from user.views import signup_normal_user, signup_super_user, signup

urlpatterns = [
    path('signup/', signup, name="signup"),
    path('user-signup/', signup_normal_user, name="user-signup"),
    path('admin-signup/', signup_super_user, name="admin-signup"),
]
