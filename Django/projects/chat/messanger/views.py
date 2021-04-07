from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import *
from login.models import User


def get_request_information(request):
    name = User.objects.get(username=request.session['username'])
    request_information = {}
    request_information['recieved_requests'] = {RequestsToFriendList.objects.filter(request_to=name.iduser)[i].pk: RequestsToFriendList.objects.filter(request_to=name.iduser)[i].request_from.username for i in range(len(RequestsToFriendList.objects.filter(request_to=name.iduser)))}
    request_information['send_requests'] = {RequestsToFriendList.objects.filter(request_from=name.iduser)[i].pk: RequestsToFriendList.objects.filter(request_from=name.iduser)[i].request_to.username for i in range(len(RequestsToFriendList.objects.filter(request_from=name.iduser)))}
    return request_information


def become_friends(request):
    request = RequestsToFriendList.objects.get(pk=request.POST['pk'])
    new_friends = Friends()
    new_friends.friend1 = User.objects.get(pk=request.request_from.pk)
    new_friends.friend2 = User.objects.get(pk=request.request_to.pk)
    new_friends.save()
    new_friends1 = Friends()
    new_friends1.friend1 = User.objects.get(pk=request.request_to.pk)
    new_friends1.friend2 = User.objects.get(pk=request.request_from.pk)
    new_friends1.save()
    new_chat = Chat()
    new_chat.friend1 = User.objects.get(pk=request.request_from.pk)
    new_chat.friend2 = User.objects.get(pk=request.request_to.pk)
    new_chat.save()
    request.delete()


def get_friends(request):
    name = User.objects.get(username=request.session['username']).pk
    list_of_friends = {}
    list_of_friends['list_of_friends'] = {}
    for idfriendlist in Friends.objects.filter(friend1=name):
        friend2 = Friends.objects.get(pk=idfriendlist.pk).friend2
        username = User.objects.get(pk=friend2.pk).username
        list_of_friends['list_of_friends'].update({idfriendlist.pk: username})
    return list_of_friends


def get_chat_history(request, friend2):
    friend1 = User.objects.get(username=request.session['username']).pk
    friend2 = User.objects.get(username=friend2).pk
    idchat = request.session['idchat']  # реализовать единсвенное обращение к бд за idchat (сейчас при каждом отправленном сообщении)
    chat_history = {}  # ^ сделанно в get_idchat(), поменять обращения в коде ^
    chat_history['chat_history'] = {}
    print(Message.objects.filter(idchat=idchat).order_by('idmessage'))
    for i in Message.objects.filter(idchat=idchat).order_by('idmessage')[::-1][:50][::-1]:  # сделать подзагрузку сообщений по необходимости
        chat_history['chat_history'].update({i.pk: {'from_friend': i.from_friend.username, 'date_message': i.date_message, 'text': Text.objects.get(idmessage=i.pk).text}})
    if not len(chat_history['chat_history']):
        chat_history['chat_history'] = {'0': {'text': 'Nothing here, yet...'}}
    return chat_history


def send_message(request, text):
    try:
        idchat = Chat.objects.get(friend1=User.objects.get(username=request.session['username']).pk, friend2=User.objects.get(username=request.session['to']).pk)  # подумать реализацией единсвенного обращение к бд за idchat (сейчас при каждом отправленном сообщении & обновлении истории сообщений)
    except Exception:
        idchat = Chat.objects.get(friend1=User.objects.get(username=request.session['to']).pk, friend2=User.objects.get(username=request.session['username']).pk)
    # idchat = request.session['idchat']
    # не получяается записать в бд idchat, тк является интом, а не классом Model.Chat
    print(type(idchat))
    new_message = Message()
    new_message.from_friend = User.objects.get(username=request.session['username'])
    new_message.to_friend = User.objects.get(username=request.session['to'])
    new_message.idchat = idchat
    new_message.save()
    new_text = Text()
    new_text.text = text
    new_text.idmessage = Message.objects.get(pk=new_message.pk)
    new_text.save()
    return get_chat_history(request, request.session['to'])


def get_idchat(request, user_to):
    user_from = request.session['id_user']
    user_to = User.objects.get(username=user_to)
    try:
        request.session['idchat'] = Chat.objects.get(friend1=user_from, friend2=user_to).pk
    except Exception:
        request.session['idchat'] = Chat.objects.get(friend1=user_to, friend2=user_from).pk


def messanger(request):
    if 'username' in request.session:
        content = {}
        try:
            content['list_of_friends'] = get_friends(request)
        except Exception:
            pass
        if 'find_user' in request.POST:
            return render(request, 'messanger/find_user.html')
        elif 'find' in request.POST:
            name = '0'
            if request.POST['searched_name'] != request.session['username']:
                try:
                    name = User.objects.get(username=request.POST['searched_name'])
                    request.session['request_to_id'] = name.iduser
                    return render(request, 'messanger/find_user.html', {'name': name.username})
                except Exception:
                    return render(request, 'messanger/find_user.html', {'name': name})
            else:
                return render(request, 'messanger/find_user.html', {'name': name})
        elif 'add_user' in request.POST:
            print(request.session['username'])
            friend1 = User.objects.get(username=request.session['username'])
            friend2 = User.objects.get(iduser=request.session['request_to_id']).iduser
            if RequestsToFriendList.objects.filter(request_from=friend1.iduser, request_to=friend2):
                return render(request, 'messanger/find_user.html', {'name': '1'})
            elif RequestsToFriendList.objects.filter(request_to=friend1.iduser, request_from=friend2):
                return render(request, 'messanger/find_user.html', {'name': '1'})
            if Friends.objects.filter(friend1=friend1.iduser, friend2=friend2):
                return render(request, 'messanger/find_user.html', {'name': '2'})
            elif Friends.objects.filter(friend2=friend1.iduser, friend1=friend2):
                return render(request, 'messanger/find_user.html', {'name': '2'})
            new_friend_request = RequestsToFriendList()
            new_friend_request.request_from = User.objects.get(username=friend1.username)
            new_friend_request.request_to = User.objects.get(pk=friend2)
            new_friend_request.save()
            return render(request, 'messanger/find_user.html')
        elif 'friend_requests' in request.POST:
            try:
                request_information = get_request_information(request)
                return render(request, 'messanger/friend_requests.html', request_information)
            except Exception:
                pass
            return render(request, 'messanger/friend_requests.html')
        elif 'cancel' in request.POST:
            try:
                pk = request.POST['pk']
                friend_request = RequestsToFriendList.objects.get(pk=pk)
                friend_request.delete()
                request_information = get_request_information(request)
                return render(request, 'messanger/friend_requests.html', request_information)
            except Exception:
                request_information = get_request_information(request)
                return render(request, 'messanger/friend_requests.html', request_information)
        elif 'accept' in request.POST:
            try:
                become_friends(request)
                request_information = get_request_information(request)
                return render(request, 'messanger/friend_requests.html', request_information)
            except Exception as error:
                request_information = get_request_information(request)
                return render(request, 'messanger/friend_requests.html', request_information)
        elif 'chat' in request.POST:
            return render(request, 'messanger/messanger.html', content)
        elif 'friend' in request.POST:
            try:
                get_idchat(request, request.POST['friend'])
                request.session['to'] = request.POST['friend']
                content['chat_history'] = get_chat_history(request, request.POST['friend'])
                return render(request, 'messanger/messanger.html', content)
            except Exception as error:
                content['chat_history'] = {'0': {'text': 'Nothing here, yet...'}}
                return render(request, 'messanger/messanger.html', content)
        elif 'send' in request.POST:
            try:
                content['chat_history'] = send_message(request, request.POST['text_area'])
                return render(request, 'messanger/messanger.html', content)
            except Exception as error:
                return render(request, 'messanger/messanger.html', content)
        else:
            return render(request, 'messanger/messanger.html', content)
    else:
        return HttpResponseRedirect('login/')
