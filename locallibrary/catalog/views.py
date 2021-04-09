from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login, models
from django.contrib import messages
from django.http import HttpResponse
from .models import Line, Region, Station
from .forms import ContactForm

def client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# def homepage(request):
#     if not request.user.is_authenticated:
#         return render(request = request,
#                       template_name='main/home.html',
#                       context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all})
#     else:
#         if request.user.is_superuser:
#             return render(request = request,
#                       template_name='main/manager.html')
#         else:
#             return render(request = request,
#               template_name='main/client.html')

def manage(request):
    return render(request = request, template_name='main/manager.html')

def homepage(request):
    if request.method == "POST" or str(request.user)!='AnonymousUser':
        if str(request.user)!='AnonymousUser':
            print(22222222222222)
            return render(request = request,
              template_name='main/home.html',
              context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all})
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(11111111111111111)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                # print(type(request.POST['station']))
                # s = [i for i in Station.objects.all() if request.POST['station'] == i.__str__()][0]
                # s.station_Status = True
                # s.save()
                # return redirect('/')
                return render(request = request,
                      template_name='main/home.html',
                      context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all})
            else:
                messages.error(request, "Invalid username or password")
                return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})
        else:
            messages.error(request, "Invalid username or password")
            return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})
    else:
        form = AuthenticationForm()
        return render(request = request,
              template_name = "main/login.html",
              context={"form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                if request.user.is_superuser:
                    return render(request = request,
                                  template_name='main/home.html',
                                  context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all})
                else:
                    return render(request = request,
                                  template_name = "main/user.html")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = ContactForm()
    return render(request = request,
                  template_name = "main/login.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    # print(request.GET)
    # for i in Station.objects.all():
    #     print(i)
    #     i.station_Status = False
    #     i.save()
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def single_slug(request, single_slug):
    lines = [t.line_category for t in Line.objects.all()]
    regions = [t.region_category for t in Region.objects.all()]
    stations = [t.station_slug for t in Station.objects.all()]
    print(single_slug+'------------------------')
    print(lines)
    print(regions)
    print(stations)
    return render(request=request,
                  template_name='main/home.html')