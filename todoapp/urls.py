from django.urls import path
from .views import TodoList, TodoCreate, TodoDetail, TodoLogin, TodoLogout, TodoUpdate, TodoDelete

urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('login/', TodoLogin.as_view(), name='login'),
    path('logout/', TodoLogout.as_view(), name='logout'),
    path('add/', TodoCreate.as_view(), name='add'),
    path('<int:pk>/', TodoDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', TodoUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', TodoDelete.as_view(), name='delete'),
]
