from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.PostList,name='PostList'),
    path('<int:id>/',views.PostDetails,name='PostDetails'),
]
