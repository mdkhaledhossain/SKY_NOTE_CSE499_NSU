from django.urls import path 
from skynote_app import views 

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('index/', views.index, name='index'),
    path('library/', views.library, name='index'),
    path('', views.index, name = 'index'),
    path('test/',views.test, name = "test"),
    path('note_details/',views.note_details, name = "test")

    
]