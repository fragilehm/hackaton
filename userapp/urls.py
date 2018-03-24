from django.conf.urls import url

from .views import UserDetail, UserList


urlpatterns = [
    url(r'users/$', UserList.as_view(), name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail')
]
