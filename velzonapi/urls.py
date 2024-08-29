from django.urls import path
from velzonapi.views import getDate,user_getDate,addUsers, addState,updateState, updateUsers,deteteState,LoginView,getCity,addCity
urlpatterns = [
    path('state/', getDate, name='get_date'),
    path('users/',user_getDate,name='get_date'),
    path('city/', getCity, name='get_city'),
    path('addusers/',addUsers,name='addUsers'),
    path('addstate/',addState,name=' addState'),
    path('addcity/',addCity,name='addCity'), 
    path('updateState/<int:id>',updateState,name=' updateState'),
    path('updateUsers/<int:id>',updateUsers,name='updateUsers'), 
    path('deteteState/<int:id>',deteteState,name='deteteState'),
    
 
    
    
    
    path('login/', LoginView.as_view(), name='login'),
    # path('login1/', Login_View.as_view(), name='login1'),
]

