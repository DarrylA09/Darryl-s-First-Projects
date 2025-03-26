from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def user_login(request):
    '''
    This function renders the login page.
    '''
    return render(request, 'authentication/login.html')


def authenticate_user(request):
    '''
    This function authenticates the user.
    '''
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    # If user is None, then the user is not authenticated. Redirect
    # the user to the login page. 
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    # If user is authenticated, then log the user in and redirect the
    # user to the show_user page.
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    

def show_user(request):
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })
