from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('cars/',views.cars,name='cars'),
    path('detail/<str:pk>/',views.detail,name='detail'),
    path('detail/<str:pk>/',views.detail,name='detail'),
    path('logout/',views.logoutUser,name='logout'),
    path('personal/',views.personal,name='personal'),
    path('booking/',views.booking,name='booking'),
    path('profile/',views.profile,name='profile'),
    path('mybookings/',views.mybookings,name='mybookings'),
    path('cancel/<int:id>/',views.cancelf, name="cancel"),
    path('update/<int:id>/',views.update, name="update"),
    path('notification/',views.notify,name='notification'),
    path('feedback/',views.fdback,name='feedback'),
    path('review/',views.Review,name='review'),
    path('seemore/',views.smore, name="seemore"), 
    path('about/',views.about, name="about"), 
    path('client/',views.Client, name="clnt"), 
]
