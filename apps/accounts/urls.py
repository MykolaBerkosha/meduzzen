
from django.urls import path

from apps.accounts import views


urlpatterns = [

    path('', views.ListAPI.as_view()),

    path('<int:user_id>/', views.ObjectAPI.as_view())

]
