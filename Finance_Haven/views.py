from django.http import HttpResponse
# to return a template using the HttpResponse, we need to import the 'render' module
from django.shortcuts import render # allows us to render a html template in the browser

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')
def about(request):
    # return HttpResponse('about')
    return render(request,'about.html')
