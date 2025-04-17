from django.shortcuts import render,redirect
from .models import Catagory
from .models import Product
from django.contrib import messages
from .form import CustomUserForm
from django.contrib.auth import authenticate,login,logout


def home(request):
    products=Product.objects.filter(trending=1)
    
    return render(request,"shop/index.html",{"products":products})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('login')                   
    else:

        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get("password")
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect(request,'home')

            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect('login')
        return render(request,"shop/login.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("home") 


    
def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database (creates the new user)
            return redirect('login')  # Redirect to home page after successful registration
        else:
            # If the form is not valid, return the form with errors
            return render(request, 'shop/register.html', {'form': form})
    else:
        form = CustomUserForm()  # Initialize an empty form for GET request
    
    return render(request, 'shop/register.html', {'form': form})
    
    # form=CustomUserForm()
    # if request.method == 'POST':
    #     form = CustomUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Saves the user to the database
    #         return redirect('home')  # Redirect to the home page after successful registration
    # else:
    #     form = CustomUserForm()  # Empty form for GET request

    # return render(request, 'shop/register.html', {'form': form})

def collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"shop/collection.html",{"catagory":catagory})
def collectionsviews(request,name):
    if(Catagory.objects.filter(name=name,status=0)):
        products=Product.objects.filter(catagory__name=name)

        return render(request,"shop/products/index.html",{"products":products,"catagory_name":name})
    else:

        messages.warning(request,"no such Catagory found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Catagory Found")
            return redirect("collections")

    else:
        messages.error(request,"No Such Catagory Found")
        return redirect("collections")
# Create your views here.
