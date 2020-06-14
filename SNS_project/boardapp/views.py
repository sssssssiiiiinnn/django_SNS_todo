from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login

# Create your views here.


def signup_function(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            print(User.objects.get(username=username))
            return render(request,
                          'signup.html',
                          {'error': 'User already exist'}
                          )
        except:
            User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})


def login_function(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            print('login failure')
            return redirect('login')

    if request.method == 'GET':
        return render(request, 'login.html')


@login_required
def list_function(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logout_function(request):
    logout(request)
    # Redirect to a success page.
    return redirect('login')


def detail_function(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def good_function(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')


def read_function(request, pk):
    post = BoardModel.objects.get(pk=pk)
    user = request.user.get_username()

    if user not in post.read_text:
        post.read += 1
        post.read_text += post.read_text + ',' + user
        post.save()
    return redirect('list')
