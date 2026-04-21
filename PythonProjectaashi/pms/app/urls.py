from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('developer-dashboard/', views.developer_dashboard, name='developer_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]