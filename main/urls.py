from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from authentication import  views as auth
from django.conf.urls import url

urlpatterns = [
    path('index',views.index,name='index'),
    path('article/<int:pk>', views.article,name = 'get_article'),
    path('author/<int:pk>', views.author,name = 'get_author'),
    path('article',views.create_article,name = 'create_article'),
    path('author',views.create_author,name = 'create_author'),
    path('',views.home,name = 'home'),
    path('view_authors',views.view_authors,name = 'view_authors'),
    path('search',views.search,name = 'search'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    
    # url(r'^register/$',auth.register,name='register'),
    url(r'^login/$',auth.login,name='login')
]
