from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.login_user,name="login"),
    path('dashboard/',views.manager,name="dashboard"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('track/',views.customer,name="track"),
    path('shipments/',views.deliveryboy,name="shipments"),
    path('view-reports/',views.view_reports,name="report_manager"),
    path('create-reports/<str:id>',views.create_reports,name="create_reports"),
    path('hire_deliveryboy',views.hire_deliveryboy,name="hire_deliveryboy")
]