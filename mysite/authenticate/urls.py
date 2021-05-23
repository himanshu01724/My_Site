from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('register/',views.register,name="log"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
]
