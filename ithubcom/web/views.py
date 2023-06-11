from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import *


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        user_and_password = User.objects.create(username=request.POST.get('username'), password=request.POST.get('password'))
        user_and_password.save()

    return render(request, 'web/index.html')


@csrf_exempt
def our_users(request):

    if request.method == 'POST':
        User.objects.get(username=request.POST.get('username')).delete()
    users_and_password = User.objects.all()
    return render(request, 'web/users_and.html', {'users_and': users_and_password})



