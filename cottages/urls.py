from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('my_cottages/', views.my_cottages, name="my_cottages"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login, name="login"),
    path('<int:id>/', views.cottage_detail, name="detail"),
    path('new_cottage/', views.CottageCreate.as_view(), name="new_cottage"),
    path('<int:id>/update/', views.CottageUpdate.as_view(), name="cottage_update"),
    path('<int:pk>/delete/', views.CottageDeleteView.as_view(), name="cottage_delete"),
]


