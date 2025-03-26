from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from accounts.forms import SignUpForm


def index(request):
    """
    This function returns the latest five questions according 
    to the publication date.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/poll.html", context)


def signup(request):
    """
    This function signs up a user.
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:login')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})


def user_login(request):
    '''
    This function renders the login page.
    '''
    return render(request, 'registration/login.html')


def authenticate_user(request):
    '''
    This function authenticates the user.
    '''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            # Handle missing username or password
            return render(request, 'registration/login.html', {
                'error_message': 'Username and password are required.'
            })

        user = authenticate(username=username, password=password)

        # If user is None, then the user is not authenticated. Redirect
        # the user to the login page. 
        if user is None:
            return HttpResponseRedirect(reverse('polls:login'))
        # If user is authenticated, then log the user in and redirect the
        # user to the poll home page.
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
    else:
        return HttpResponseRedirect(reverse('polls:login'))


def detail(request, question_id):
    """
    This function returns the question with the given question_id.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    """
    This function returns the results of the question with the given 
    question_id.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    """
    This function increments the vote count of the selected choice.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully
        # dealing with POST data. This prevents data from being
        # posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )