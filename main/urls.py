from django.urls import path
from .views import (
home, profile, update_profile, search, detail 
)
urlpatterns = [
    path('home', home, name='home'),
    path("update-profile", update_profile, name="update_profile"),
    path("profile", profile, name="profile"),
    path('search', search, name='search'),
    path("detail/<int:id>", detail, name="detail")
]