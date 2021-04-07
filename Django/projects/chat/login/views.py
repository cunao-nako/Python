from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import User


def login(request):
    if 'login' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            try:
                user = User.objects.get(username=username, password=password)
                request.session['username'] = user.username
                request.session['id_user'] = user.pk
                return render(request, 'main/profile.html', {'username': request.session['username']})
            except Exception:
                message = {'message': 'Username or Password not exist'}
                return render(request, 'login/error.html', message)
        else:
            return render(request, 'login/login.html')
    elif 'signin' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            try:
                user = User.objects.get(username=username)
                message = {'message': 'Username already taken'}
                return render(request, 'login/error.html', message)
            except Exception:
                new_user = User()
                new_user.username = username
                new_user.password = password
                new_user.save()
        return render(request, 'login/login.html')
    elif 'back' in request.POST:
        return render(request, 'login/login.html')
    else:
        return render(request, 'login/login.html')
