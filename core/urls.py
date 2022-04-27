
from django.contrib import admin
from django.urls import path

from apps.accounts import views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/v1/accounts/', views.AccountsAPI.as_view())

]
