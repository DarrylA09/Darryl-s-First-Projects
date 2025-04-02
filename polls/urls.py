from django.urls import path
from . import views

# This is the URL configuration for the polls application.
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('/login/', views.login_user, name='login'),
#   path('auth/authenticate/', views.authenticate_user, name='authenticate_user'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('signup/', views.signup, name='signup'),
]