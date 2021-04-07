from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect

from login.models import User


def main(request):
    if 'username' in request.session:
        username = {'username': request.session['username']}
        if 'logout' in request.POST:
            del request.session['username']
            try:
                del request.session['to']
                return HttpResponseRedirect('login/')
            except Exception:
                return HttpResponseRedirect('login/')
        elif 'change' in request.POST:
            return render(request, 'main/change.html')
        elif 'save' in request.POST:
            print(request.POST['new_username'])
            print(request.session['username'])
            user = User.objects.get(username=request.session['username'])
            print(request.POST['new_password'], request.POST['new_username'])
            if request.POST['new_username']:
                user.username = request.POST['new_username']
                request.session['username'] = request.POST['new_username']
            elif request.POST['new_password']:
                 user.password = request.POST['new_password']
            user.save()
            return render(request, 'main/profile.html', username)
        elif 'back' in request.POST:
            return render(request, 'main/profile.html', username)
        else:
            return render(request, 'main/profile.html', username)
    else:
        return HttpResponseRedirect('login/')
