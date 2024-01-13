from django.shortcuts import render

# Create your views here.

def userfilters(request):
    d={'data':'HAI HOw ArE You'}
    return render(request,'userfilters.html',d)
    