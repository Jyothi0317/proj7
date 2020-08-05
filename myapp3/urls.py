from django.urls import path
from myapp3 import views
app_name="myapp3"

urlpatterns = [
    path('trial/',views.trial,name="trial"),
    path('profile/',views.profile,name="profile"),
]