from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('cause',views.cause,name='cause'),
    path('donate',views.donate,name='donate'),
    path('blog',views.blog,name='blog'),
    path('blogsingle',views.blogsingle,name='blogsingle'),
    path('event',views.event,name='event'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('message',views.send_message,name='message'),
    path('volregister',views.volregister,name='volregister'),
    path('',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('querymessage',views.query_message,name='query_message'),


    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),


    path('changepass',views.changepassword,name='changepass'),



]
