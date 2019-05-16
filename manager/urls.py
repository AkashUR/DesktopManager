from django.urls import path,re_path
from . import views

urlpatterns = [
    # /manager/
    path('',views.login,name='login'),
    # /manager/C/
    path('log',views.log,name='log'),
    re_path(r'^(?P<location>[A-Za-z0-9:./\s]+/)(\?delete=(?P<delete>[A-Za-z0-9:.\s]+))?$',views.listDirectory,name='listDirectory'),
]