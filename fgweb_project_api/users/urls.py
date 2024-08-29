from django.urls import path
from users.views import UsersTestViews
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('registers/', UsersTestViews.as_view()),
    path('jwt/access/',TokenObtainPairView.as_view()),
    path('jwt/refresh/',TokenRefreshView.as_view()),
    path('jwt/verify/',TokenVerifyView.as_view()),
]
