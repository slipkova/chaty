from django.urls import path
from. import views

app_name = 'cottages'

urlpatterns = [
    path('', views.index, name='index'),
    path('cottages/my_cottages', views.my_cottages, name="my_cottages"),
    path('cottages/registration', views.registration, name="registration"),
]
