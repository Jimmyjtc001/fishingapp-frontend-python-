from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


def index_page(request):

    return render(request,'homepage/homepage/index.html',{})



def contact_page(request):
    context = {}

    return render(request,'homepage/homepage/contact.html',context)
