from django.shortcuts import render
# this is the added import for responce
from django.http import HttpResponse

# Create your views here.
# home view 
def home(request):
    return HttpResponse('<h1>get going</h1>')
# this is the about function for see about dragon collector
def about(request):
    return render(request, 'about.html')
def dragon_index(request):
    return render(request, 'dragons/index.html', {'dragons': dragons})




