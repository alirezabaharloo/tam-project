from django.urls import path
from .. import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='user-detail'),
    path('update_profile/<int:pk>', views.ProfileView.as_view(), name='update-profile'),
]

