# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Bonjour tout le monde !")


from django.shortcuts import render

def index(request):
    return render(request, "notes/index.html")

