from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == "post":
        pass
    return render(request, 'web/index.html')

