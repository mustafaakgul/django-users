from django.urls import path
from account.views import *

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('home/', home, name="home"),
    path('profile/', account_view, name="account"),
]