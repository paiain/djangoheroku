from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello This is homework 4 and 5 consist of index,about,contect,persons')
def about(request):
    return HttpResponse('helol about pages')
def contect(request):
    return HttpResponse('helol contect pages')
def persons(request):
    return HttpResponse('helol persons pages')
