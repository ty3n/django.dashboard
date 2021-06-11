from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login, models
from django.contrib import messages
from django.http import HttpResponse
from .models import Line, Region, Station
from .forms import ContactForm, FileUploadForm, UploadForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
import giteapy

class FileUploadView(APIView):
    parser_classes = [FileUploadParser, ]
    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        with open(filename, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
        return Response(f'{filename} uploaded',status=204)
    def post(self,request,filename,format=None):
        form = UploadForm(request.POST or None, request.FILES or None)
        context = {'form':form}
        return render(request, '', context)
    def get(self,request,filename,format=None):
        print(request)
        return HttpResponseRedirect('/')

class Gitea:
    def __init__(self,host,user,pwd):
        self.conf = giteapy.Configuration()
        self.conf.host = host
        self.conf.username = user
        self.conf.password = pwd
        self.adminapi = giteapy.AdminApi(giteapy.ApiClient(self.conf))
        self.repoapi = giteapy.RepositoryApi(giteapy.ApiClient(self.conf))
    def creatRepo(self,repo):
        repoadd = giteapy.CreateRepoOption(name=repo)
        self.adminapi = self.adminapi.admin_create_repo('hitron',repoadd)
    def checkRepo(self,repo):
        return self.repoapi.repo_get('hitron',repo)
    def checkRepoBranch(self,repo,branch):
        return self.repoapi.repo_get_branch('hitron',repo,branch)

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

@login_required(login_url='/')
def manage(request):
    return render(request = request, template_name='main/manager.html')

class HomePage(View):
    def get(self,request,*args,**kwargs):
        if str(request.user)!='AnonymousUser':
            uform = UploadForm(request.POST or None, request.FILES or None)
            if request.is_ajax():
                if form.is_valid():
                    form.save()
                    return JsonResponse({'message':'hell yeah'})
            return render(request = request,
              template_name='main/home.html',
              context={"form":uform})
        form = AuthenticationForm()
        return render(request = request,
              template_name = "main/login.html",
              context={"form":form})
    def post(self,request,*args,**kwargs):
        uform = UploadForm(request.POST or None, request.FILES or None)
        if request.is_ajax():
            if uform.is_valid():
                uform.save()
                return JsonResponse({'message':'hell yeah'})
        if str(request.user)!='AnonymousUser':
            return render(request = request,
              template_name='main/home.html',
              context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all})
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
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
                      context = {"lines":Line.objects.all, "regions":Region.objects.all, "stations":Station.objects.all,"form":uform})
            else:
                messages.error(request, "Invalid username or password")
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

# def single_slug(request, single_slug):
#     lines = [t.line_category for t in Line.objects.all()]
#     regions = [t.region_category for t in Region.objects.all()]
#     stations = [t.station_slug for t in Station.objects.all()]
#     print(single_slug+'------------------------')
#     print(lines)
#     print(regions)
#     print(stations)
#     return render(request=request,
#                   template_name='main/home.html')

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers":10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self , request, format=None):
        g = Gitea('http://172.18.130.11:3000/api/v1','hitron','hitron')
        d = g.repoapi.repo_search()
        s = sorted([s.updated_at.date().__str__() for s in d.data])
        q = sorted([s.created_at.date().__str__() for s in d.data])
        data = {}
        for i in s:
            if i in data.keys():
                data[i] += 1
            else:
                data.update({i:1})
        # data = {
        #     'a':[1,2,3,4],
        #     'b':[5,6,7,8]
        # }
        return Response(data)