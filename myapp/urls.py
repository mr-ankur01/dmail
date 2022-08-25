from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('sign/',views.sign,name='sign'),
    path('login/',views.loginUser,name='login'),
    path('message/<int:id>',views.message,name='message'),
    path('download/<int:id>',views.download,name='download'),
    path('delmsg/<int:id>',views.delmsg,name='delmsg'),
    path('docs/',views.docs,name='docs'),
    path('forget-password/',views.forget,name='forget'),
    path('change-password/<token>/',views.changePass,name='changePassword'),
    path('custom/',views.custom,name='custom'),
    path('change/',views.change,name='change'),
    path('logout/',views.logoutUser,name='logout'),
    path('ex/',views.ex,name='ex')
    
]