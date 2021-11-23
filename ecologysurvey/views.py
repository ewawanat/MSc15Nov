from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homePage(request):
#    return HttpResponse('Hi there birder!')
    return render(request, 'homepage.html')
