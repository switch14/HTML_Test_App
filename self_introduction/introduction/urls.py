from django.urls import path
from . import views

app_name = 'introduction'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('register/<int:pk>/',views.RegisterDetailView.as_view(),name='register_detail'),
]