from django.urls import path

from users.views import Users

urlpatterns = [
    path('', Users.as_view())
]