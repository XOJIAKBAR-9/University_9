from django.shortcuts import render, redirect
from django.contrib import redirects
from django.template.context_processors import request

from Uniapp.forms import *
from models import *


def ustoz_search(request):
    search = request.GET.get('search', None)
    ustoz_search = Ustoz.objects.all()
    if search is not None:
        ustoz_search = Ustoz.objects.filter(ism__icontains=search).order_by('ism')
        context = {
            'ustoz_search': ustoz_search
        }
        return render(request, "ustoz_Search", context)


def Fan_form(request):
    form = Fan_form()
    if request.method=="POST":
        form_data=Fan_form()
        if form_data.is_valid():
            form_data.save()
        return redirect(Fan)
    context={
        'form':form
    }
    return redirect(request,"Fan_form.html", context)



def Yonalish_form(request):
    form = Yonalish_form()
    if request.method=="POST":
        form_data=Yonalish_form()
        if form_data.is_valid():
            form_data.save()
        return redirect(Yonalish)
    context={
        'form':form
    }
    return redirect(request,"Yonalish_form.html", context)
