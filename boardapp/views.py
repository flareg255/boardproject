from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import BoardModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


def signupFunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username2, '', password2)
            return redirect('login')

    return render(request, 'signup.html', {'some': 100})


def loginFunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')

    return render(request, 'login.html', {'some': 100})


@login_required
def listFunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logoutFunc(request):
    logout(request)
    return redirect('login')


def detailFunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodFunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good = post.good + 1
    post.save()
    return redirect('list')


def readFunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext = post.readtext + ' ' + post2
        post.save()
        return redirect('list')


class createClass(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('list')
