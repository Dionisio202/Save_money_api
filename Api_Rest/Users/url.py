from django.urls import path
from . import views
from knox import views as knox_views
urlpatterns=[
    path('login/',views.login_api),#Hay que enviar los datos por el emtodo POST para logearse en
    path('user/',views.get_user_data),#Busca un usuario por
    path('register/',views.register_api),#envia un metodo POST par crear un usuario en raw 
    path('logout/',knox_views.LogoutView.as_view()),
    path('logoutall',knox_views.LogoutAllView.as_view())
]