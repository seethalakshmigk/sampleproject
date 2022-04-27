from django.urls import path
from . import views

urlpatterns = [
    path('samplefn',views.samplefn),
    path('firstpage',views.firstfn)

    
]