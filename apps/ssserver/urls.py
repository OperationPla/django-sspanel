# from django.conf.urls import url
from django.urls import path
from .import views


app_name = "ssserver"
urlpatterns = [
    path('changesspass/', views.ChangeSsPass, name='changesspass'),
    path('user/edit/<int:pk>/', views.User_edit, name='user_edit'),
    path('changessmethod/', views.ChangeSsMethod, name='changessmethod'),
    path('changessprotocol/', views.ChangeSsProtocol, name='changessprotocol'),
    path('changessobfs/', views.ChangeSsObfs, name='changessobfs'),
    path('subscribe/<token>/', views.subscribe, name='subscribe'),
    path('node/config/', views.node_config, name='node_config'),
]
