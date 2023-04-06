from django.urls import path
from . import views

urlpatterns = [
    path('',views.default),
    path('home',views.default),
    path('subjects',views.subjects),
    path('view1', views.view1),
    path('view3', views.view3),
    path('view2', views.view2),
]