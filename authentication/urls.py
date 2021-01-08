from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('register/',views.register,name='register'),
    # path('login/',views.login,name='login')

    url('register',views.register,name='register'),
]