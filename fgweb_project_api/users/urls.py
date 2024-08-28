from django.urls import path
from users.views import UsersTestViews

urlpatterns = [
    path('registers/', UsersTestViews.as_view()),
]
