from apps.users import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^usernames/(?P<username>\w{5,20})/count/$', views.RegisterUsernameCountView.as_view(), name='usernamecount')
]
