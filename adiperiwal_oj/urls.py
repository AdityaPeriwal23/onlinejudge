from django.urls import path

from . import views

urlpatterns = [
    path('',views.options,name='options'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('signincheck/',views.signincheck,name='signincheck'),
    path('logincheck/',views.logincheck,name='logincheck'),
    path('<int:user_id>/', views.index, name='index'),
    path('<int:user_id>/allsubmissionslist/',views.allsubmissionslist,name='allsubmissionslist'),
    path('<int:problem_id>/<int:user_id>/', views.detail, name='detail'),
    path('<int:problem_id>/code/<int:user_id>/', views.code, name='code'),
    path('<int:problem_id>/history/<int:user_id>/', views.history, name='history'),
    path('<int:problem_id>/particular/<int:submission_id>/<int:user_id>/', views.particular, name='particular'),
]