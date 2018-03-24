from django.conf.urls import url

from .views import UserDetail, OrganizationList


urlpatterns = [
    url(r'organizations/$', OrganizationList.as_view(), name='organization-list'),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail')
]
