from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.login_user,name='login'),
    path("check/",views.base,name='base'),

]