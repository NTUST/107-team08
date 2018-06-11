# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response,render,redirect
from .models import *
@csrf_exempt

def index(request):
	comment=Comment_for_nightmarket.objects.all();
	return render(request,'index.html',locals())
def gallery(request):
	return render(request,'gallery.html',locals())
def generic(request):
	return render(request,'generic.html',locals())
def contact(request):
	return render(request,'contact.html',locals())
def submit(request):
	name=''
	message=''
	if request.method == 'POST':
		name = request.POST.get('name')
		message = request.POST.get('message')
		#comment.objects.create(name=name, message=message)
		#comment.save()
		Comment.objects.create(name=name, message=message)
		#return redirect('/contact/')
	return render(request,'contact.html',locals())
def nightmarket_submit(request):
	name=''
	message=''
	selection=''
	if request.method == 'POST':
		name = request.POST.get('name')
		message = request.POST.get('message')
		selection=request.POST.get('selection')
		Comment_for_nightmarket.objects.create(name=name, message=message,nightmarket_name=selection)
	return render(request,'gallery.html',locals())
def a1(request):
	return render(request,'a1.html',locals())
def a2(request):
	return render(request,'a2.html',locals())
def a3(request):
	return render(request,'a3.html',locals())
def a4(request):
	return render(request,'a4.html',locals())
def a5(request):
	return render(request,'a5.html',locals())
def a6(request):
	return render(request,'a6.html',locals())
def a7(request):
	return render(request,'a7.html',locals())
