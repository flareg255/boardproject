from django.urls import path
from .views import signupFunc, loginFunc, listFunc, logoutFunc, detailFunc, goodFunc, readFunc, createClass

urlpatterns = [
    path('signup/', signupFunc, name='signup'),
    path('login/', loginFunc, name='login'),
    path('list/', listFunc, name='list'),
    path('logout/', logoutFunc, name='logout'),
    path('detail/<int:pk>', detailFunc, name='detail'),
    path('good/<int:pk>', goodFunc, name='good'),
    path('read/<int:pk>', readFunc, name='read'),
    path('create/', createClass.as_view(), name='create'),
]
