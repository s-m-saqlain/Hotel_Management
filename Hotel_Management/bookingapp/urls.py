from django.urls import path,include
from .views import slider_view,signup,_login
urlpatterns = [

    path('',slider_view, name='slider'),
    path('signup/',signup,name="signup"),
    path('login/',_login,name="login")
]
