from django.urls import path
from .views import current_user, UserList
from rest_framework_simplejwt import views as jwt_views

from . import views
urlpatterns = [
    path('auth-token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('insertHR/',views.insertHR,name='insertHR'),

    path('get_users/',views.get_users,name="get_users"),
    path('get_user/', views.get_user, name="get_user"),
    path('insert_user/',views.insert_user,name='insert_user'),
    path('update_user/',views.update_user,name='update_user'),
]