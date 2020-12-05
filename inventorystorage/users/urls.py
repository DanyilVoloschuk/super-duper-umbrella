from django.urls import path

from users.views import Users, UsersListView

urlpatterns = [
    path('', Users.as_view()),
    path('users_list/', UsersListView.as_view())
]