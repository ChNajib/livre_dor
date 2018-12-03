import datetime

from django.contrib.auth import authenticate,login,logout

from home.forms import MessageForm, UserForm
from .models import Message
from django.shortcuts import render, get_object_or_404
import sib_sdk
import sib_api_v3_sdk
import sib_api_v3_sdk.models.send_template_email


##########  REDIRECTING TO HOME PAGE ##########

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login_user.html')

    else:
        all_messages = Message.objects.all()
        is_staff = False
        if request.user.is_staff :
            is_staff = True
        context = {'all_messages' : all_messages,
                   'current_user':request.user,
                   'is_staff':is_staff}
        return render(request,'home/index.html',context)

##########  CREATING NEW MESSAGES ##########

def create_message(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login_user.html')
    else:
        form = MessageForm(request.POST or None)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.date = datetime.datetime.now().strftime('%d %b %H:%M')
            message.save()
            send_email = sib_api_v3_sdk.SendEmail([message.user.email])
            configuration = sib_api_v3_sdk.Configuration()
            api_instance = sib_api_v3_sdk.SMTPApi(sib_api_v3_sdk.ApiClient(configuration))
            api_instance.send_template(2,send_email)
            return render(request, 'home/index.html', {'all_messages': Message.objects.all(),'current_user': request.user})
        return render(request, 'home/message_form.html', {'form': form})


##########  DELETING EXISTING MESSAGES ##########

def delete_message(request, message_id):
    msg = Message.objects.get(pk=message_id)
    user_messages = Message.objects.filter(user=request.user)
    all_messages = Message.objects.all()
    is_staff = False
    if request.user.is_staff:
        is_staff = True
    if msg.user == request.user or request.user.is_staff:
        msg.delete()
        # return render(request, 'home/index.html',{'all_messages':all_messages})
    context ={'all_messages': all_messages,
              'current_user': request.user,
              'user_messages' : user_messages,
              'is_staff':is_staff}
    return render(request, 'home/index.html', context)
##################################################


# def update_message(request, message_id,title,content):
#     msg = Message.objects.get(pk=message_id)
#     user_messages = Message.objects.filter(user=request.user)
#     all_messages = Message.objects.all()
#     if msg.user == request.user :
#         if(title != None and content!= None):
#             msg.title = title
#             msg.content = content
#         # return render(request, 'home/index.html',{'all_messages':all_messages})
#     context ={'all_messages': all_messages,
#               'current_user': request.user,
#               'user_messages' : user_messages}
#     return render(request, 'home/index.html', context)

##########  USER LOGIN ##########

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        is_staff = False
        if request.user.is_staff :
            is_staff = True
        if user is not None:
            if user.is_active:
                login(request, user)
                # messages = Message.objects.filter(user=request.user)
                return render(request, 'home/index.html' , {'all_messages' : Message.objects.all(),'current_user': request.user,'is_staff':is_staff})
            else:
                return render(request, 'home/login_user.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'home/login_user.html')


##########  CREATING NEW ACCOUNT ##########

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages = Message.objects.all()
                return render(request, 'home/index.html', {'all_messages': messages,'current_user': request.user})
    context = {
        "form": form,
        "user_is_in":request.user.is_authenticated(),
    }
    return render(request, 'home/register.html', context)
###########################################

##########  USER LOGOUT ##########

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login_user.html', context)
