from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = auth.authenticate(
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully login")
                return redirect('dashboard')
            else:
                messages.error(request, "Either username or password is not correct")
                return redirect('login')
        else:
            messages.error(request, "All fields are required")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You have successfully logout")
        return redirect('index')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if first_name and last_name and username and email and password:
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "The username has been taken")
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.error(request, "The email already exist")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            password=password
                        )
                        user.save()
                        messages.success(request, "You have successfully register user")
                        return redirect('login')
            else:
                messages.error(request, "The passwords do not match")
                return redirect('register')
        else:
            messages.error(request, "All fields are required")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)


