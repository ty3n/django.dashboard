from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns= [
	# path('admin/', admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    path("api/chart/data/",views.ChartData.as_view(),name="api-data"),
    # path("api/chart/data/",views.get_data,name="api-data"),
    path('manager/', views.manage, name="manager"),
    path("logout/", views.logout_request, name="logout"),
    # path("<single_slug>", views.single_slug, name="single_slug"),
]
