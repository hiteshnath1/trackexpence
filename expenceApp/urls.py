from django.urls import path
from .views import moneyView,charts,addmoney,my_profile_view,datatable,multiadd,multiaddsave
app_name = 'expenceApp'

urlpatterns = [
    path('',moneyView,name='home'),
    path('add/',addmoney,name='addExp'),
    path('charts/',charts,name='charts'),
    path('profile/',my_profile_view,name='profile'),
    path('datatable/',datatable,name='datatable'),
    path('addmul/',multiadd,name='addmul'),
    path('addmul/<int:pk>',multiaddsave,name='multiaddsave'),

    # path('create_multi/<str:pk>/',create_multiple,name='create_multiple'),
]