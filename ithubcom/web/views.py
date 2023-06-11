from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        user_and_password = User.objects.create(username=request.POST.get('username'), password=request.POST.get('password'))
        user_and_password.save()

    return render(request, 'web/reg.html')


@csrf_exempt
def our_users(request):

    if request.method == 'POST':
        if 'edit' in request.POST:
            object_user = User.objects.get(username=request.POST.get('username'))
            object_user.field = request.POST.get('edit_name')
            object_user.save()
        elif 'delete' in request.POST:
            User.objects.get(username=request.POST.get('username')).delete()
    users_and_password = User.objects.all()
    return render(request, 'web/users.html', {'users_and': users_and_password})


@csrf_exempt
def edit_user(request):

    # if request.method == 'POST':
    #     User.objects.get(username=request.POST.get('username')).delete()
    # users_and_password = User.objects.all()
    return render(request, 'web/edit_users.html')


