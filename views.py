# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages
# from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# def home(request):
#     return render(request, 'main/home.html')

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email    = request.POST['email']
#         password = request.POST['password']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already taken.')
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already registered.')
#         else:
#             User.objects.create_user(username=username, email=email, password=password)
#             messages.success(request, 'Account created successfully!')
#             return redirect('login')

#     return render(request, 'main/register.html')


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
        
#         user = authenticate(request, username=username, password=password)
#         if user:
#             auth_login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid credentials')
    
#     return render(request, 'main/login.html')


# def logout_view(request):
#     auth_logout(request)
#     return redirect('home')

# def amazing(request):
#     return render(request, 'main/amazingviews.html')

# def beachfront(request):
#     return render(request, 'main/beachfront.html')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    return render(request, 'main/home.html')

def cozy(request):
    return render(request, "main/cozycottage.html")

def house(request):
    return render (request, "main/houseboat.html")

def amazing(request):
    return render(request, 'main/amazingviews.html')

def beachfront(request):
    return render(request, 'main/beachfront.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email    = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully!')
            return redirect('login')

    return render(request, 'main/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'main/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('home')
