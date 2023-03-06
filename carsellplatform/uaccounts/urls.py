from django.urls import path
from .views import login, logout, register, DashboardView, UsercarsView, AddCommentView



urlpatterns = [
    path("login", login, name='login'),
    path("logout", logout, name='logout'),
    path("register", register, name='register'),
    path("dashboard", DashboardView.as_view(), name='dashboard'),
    path("user_cars", UsercarsView.as_view(), name='user_cars'),
    path("add_comment/<uuid:pk>", AddCommentView.as_view(), name='add_comment'),
]
