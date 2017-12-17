from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Customer
from .form import PostForm



# Create your views here.
def index(request):
	return render(request, 'app/index.html')

def result(request):
	customers = Customer.objects.all()
	context = {'customers' : customers}

	return render(request, 'app/result.html', context)

def post(request):

	customers = Customer.objects.all()
	context = {'customers' : customers}
	
	if request.method == 'POST':
		form = PostForm(request.POST)
		
		if form.is_valid():
			customer = form.save(commit = False) # 중복방지
			customer.ip = request.META['REMOTE_ADDR']
			customer.save()
			
			return render(request,'app/result.html', context);
	else:
		form = PostForm()
	
	return render(request, 'app/form.html', {"form":form})

def analysis(request):
	return render(request, 'app/analysis.html')

def chatbot(request):
	return render(request, 'app/chatbot.html')