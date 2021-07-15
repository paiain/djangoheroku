from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello This is homework 4 and 5 consist of index,about,contact,persons')
def about(request):
    return HttpResponse('helol about pages')
def contact(request):
    return HttpResponse('helol contact pages')
def persons(request):
    return HttpResponse('helol persons pages')


