from django.http import HttpRespose

def index(request):
    return HttpResponse("<h1>This is my music page</h1>")
