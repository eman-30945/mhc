from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('emp_form', views.emp_form , name='emp_form'),
    path('dept_log/', views.dept_log , name='dept_log'),
    path('dept_logout/', views.dept_logout , name='dept_logout'),
    path('dept_confirm/<slug:slug>/<int:id>', views.dept_confirm , name='dept_confirm'),
    path('dept_check/<slug:slug>/', views.dept_check , name='dept_check'),
    path('c_empcheck/', views.c_empcheck , name='c_empcheck'),
    path('c_currentstat/<int:id>/<slug:slug>/', views.c_currentstat , name='c_currentstat'),
    path('c_all/<int:id>/', views.c_all , name='c_all'),
    path('Subscriber/', views.Subscriber , name='Subscriber'),

]