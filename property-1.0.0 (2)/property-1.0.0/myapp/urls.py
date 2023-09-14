from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),

    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('fpswd',views.fpswd,name='fpswd'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_pswd',views.set_pswd,name='set_pswd'),

    # members
    path('add_members',views.add_members,name='add_members'),
    path('members',views.members,name='members'),
    path('delete_members/<int:pk>',views.delete_members,name='delete_members'),

    # chairmans
    path('add_chairmans',views.add_chairmans,name='add_chairmans'),
    path('chairmans',views.chairmans,name='chairmans'),
    path('delete_chairmans/<int:pk>',views.delete_chairmans,name='delete_chairmans'),

    # watchmans
    path('add_watchmans',views.add_watchmans,name='add_watchmans'),
    path('watchmans',views.watchmans,name='watchmans'),
    path('delete_watchmans/<int:pk>',views.delete_watchmans,name='delete_watchmans'),

    # visitors
    path('add_visitors',views.add_visitors,name='add_visitors'),
    path('visitors',views.visitors,name='visitors'),
    path('delete_visitors/<int:pk>',views.delete_visitors,name='delete_visitors'),

    # events
    path('add_events',views.add_events,name='add_events'),
    path('events',views.events,name='events'),
    path('delete_events/<int:pk>',views.delete_events,name='delete_events'),

    # notices
    path('add_notices',views.add_notices,name='add_notices'),
    path('notices',views.notices,name='notices'),
    path('delete_notices/<int:pk>',views.delete_notices,name='delete_notices'),

]
