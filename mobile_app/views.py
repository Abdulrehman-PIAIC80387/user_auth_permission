from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group


@login_required(login_url="/login")
def dashboard(request):
    queryset = person.objects.all()
    context = {"queryset": queryset,}
    name = "Hammad"
    email = "hamad@gmail.com"       
    web = "www.hamad.com"
    dob = "jan-1-1900"
    address="sialkot"     
    context = {
   "queryset": queryset,
    "email":email,
    "web":web,
    "dob":dob,
    "address":address,
    "name":name,
    }

    
    return render(request,"home.html",context)




def database(request):
    queryset = person.objects.all()
    context = {"queryset": queryset,}
    return render(request, "list_invoice.html", context) 


def add_invoice(request):
    
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/dashboard')
    context = {
		"form": form,
		"title": "New Invoice",
	}
    return render(request, "entry.html", context)
    

@login_required(login_url="/login")		
@permission_required("mobile_app.view_person", login_url="/login", raise_exception=True)
def list_invoice(request):
	print("in view------------------------")

	queryset = person.objects.all()
	
	
	context = {
		
		"queryset": queryset,
		
	}

	
	return render(request, "list_invoice.html", context) 


def update_invoice(request, pk):
	queryset = person.objects.get(id=pk)
	form = InvoiceUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InvoiceUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/dashboard')

	context = {
		'form':form
	}
	return render(request, 'entry.html', context)


def delete_invoice(request, pk):
	queryset = person.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/dashboard')
	return render(request, 'delete.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('dashboard')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('dashboard')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')
