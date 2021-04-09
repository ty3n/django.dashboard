from django.urls import path, include
from . import views

urlpatterns= [
    path("", views.homepage, name="home"),
    path('manager/', views.manage, name="manager"),
    path("logout/", views.logout_request, name="logout"),
    # path("<single_slug>", views.single_slug, name="single_slug"),
]
