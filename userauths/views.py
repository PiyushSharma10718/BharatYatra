from django.shortcuts import redirect, render

# Create your views here.

from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User

# User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        # print("User Registered !")
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hello, {username}, Your Account has been Created Successfully !\nWelcome to bharatYatra !")
            new_user = authenticate(username = form.cleaned_data['email'],password = form.cleaned_data['password1'])
            login(request, new_user)
            return redirect("core:index")

    else:
        form = UserRegisterForm()
        # print("User Not Registered !")

    context = {
        'form': form
    }

    return render(request, "userauths/sign-up.html", context)

    # try:
    #     if request.method == "POST":
            # dataDict = {}
            # fname = request.POST.get('fname')
            # lname = request.POST.get('lname')
            # email = request.POST.get('email')
            # password = request.POST.get('password')
            # city = request.POST.get('city')
            # country = request.POST.get('country')
            # gender = request.POST.get('gender')

            # saveData = manageUsers(fname = fname, lname = lname, email = email, password = password, city = city, country = country, gender = gender)
            # saveData.save()
            # new_user = saveData.save()
            # username = saveData.cleaned_data.get("username")
            # messages.success(request, f"Welcome {username}, Your Account has Been created Successfully and \nWelcome to BharatYatra !")
            # new_user = authenticate(username = saveData.cleaned_data['email'],
            #                         password = saveData.cleaned_data['password1']
            # )
            # login(request, new_user)

    #         dataDict = {
    #             saveData:'dataDict'
    #         }

    #         return render(request, "core:index", dataDict)
    # except:
    #     pass
    # return render(request, "userauths/sign-up.html")

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "Hey, you are Already Logged In !")
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You Logged In !")
                return redirect("core:index")
            else:
                messages.warning(request, "User Does Not Exists ! Create an Account. ")
        except:
            messages.warning(request, f"User with the {email} Does Not Exists !")

    return render(request, "userauths/sign-in.html")

def logout_view(request):
    logout(request)
    messages.success(request, "You Logged Out ! ")
    return redirect("userauths:sign-in")
