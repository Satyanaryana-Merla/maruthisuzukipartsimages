from django.shortcuts import render, redirect # type: ignore
from .models import Products, CarModel
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.db.models import Q

# def search(request):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         searched = Products.objects.filter(Q(part_ID__icontains=searched) | Q(Part_name__icontains=searched))
#         if not searched:
#             messages.success(request, "The Product doesnot exists")
#             return render(request, "search.html", {})
#         else:
#             return render(request, "search.html", {'searched':searched})
#     else:
#         return render(request, "search.html", {})
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched', '')  # Provide a default value if the key doesn't exist
        if searched:
            results = Products.objects.filter(Q(part_ID__icontains=searched) | Q(Part_name__icontains=searched))
            if not results:
                messages.error(request, "No product found.")
            return render(request, "search.html", {'searched': searched, 'results': results})
        else:
            messages.error(request, "Please enter a search term.")
    return render(request, "search.html", {})



def category(request, foo):
    foo = foo.replace('-', '')
    try:
        category = CarModel.objects.get(name=foo)
        products =Products.objects.filter(category=category)
        return render(request, 'category.html', {'products':products})

    except:
        messages.success(request, ("The category Doesn't exists"))
        return redirect('product')

def product_view(request, pk):
    product_id = Products.objects.get(id=pk)
    return render(request, 'product_view.html', {'product_id':product_id})

def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# first_name = form.cleaned_data['first_name']
			# second_name = form.cleaned_data['second_name']
			# email = form.cleaned_data['email']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ("You have successfully registered! Welcome!"))
			return redirect('home')
	
	return render(request, "register.html", {'form':form})

def register(request):
    return render(request, 'register.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Loggedin"))
            return redirect('home')
        else:
            messages.success(request, ("there was an erreor please tryafain"))
            return render('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, ("You are loggedout sucessfully"))
    return redirect('home')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # Perform further actions, such as sending an email
            return render(request, 'success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def product(request):
    products = Products.objects.all()
    return render(request, "product.html", {'products':products})


def base(request):
    return render(request, "base.html", {})
