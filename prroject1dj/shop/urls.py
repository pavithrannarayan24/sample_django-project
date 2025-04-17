from django.urls import path
from .views import *
from .import views

urlpatterns=[
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path("logout/",views.logout_page,name="logout"),
    
    path('collections/',views.collections,name="collections"),
    path('collections/<str:name>',views.collectionsviews,name="collections"),
    path('collections/<str:cname>/<str:pname>',views.product_details,name="product_details"),
    

]