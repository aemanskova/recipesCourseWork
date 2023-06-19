from django.urls import path

from users.views import UserList, UserDetail, CurrentUser

app_name = 'users'

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("users/current/", CurrentUser.as_view()),
]
