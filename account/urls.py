from django.urls import path
from .views import *


urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', SignInView.as_view(), name='login')
]
