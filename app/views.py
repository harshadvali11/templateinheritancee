from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,'parent.html')


def child(request):
    return render(request,'child.html')