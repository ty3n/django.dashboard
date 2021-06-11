from django.urls import path, include, re_path
from django.contrib import admin
from . import views

urlpatterns= [
	# path('admin/', admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    path("api/chart/data/",views.ChartData.as_view(),name="api-data"),
    path('manager/', views.manage, name="manager"),
    path("logout/", views.logout_request, name="logout"),
    re_path(r'^files/(?P<filename>[^/]+)$', views.FileUploadView.as_view()),
    # path("<single_slug>", views.single_slug, name="single_slug"),
]
