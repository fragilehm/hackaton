from django.conf.urls import url

from .views import CategoryList, MarkerListByCategoryID, MarkerDetail


urlpatterns = [
    url(r'categories/$', CategoryList.as_view(), name='category-list'),
    url(r'categories/(?P<pk>[0-9]+)/$', MarkerListByCategoryID.as_view(), name='marker-list-by-category-id'),
    url(r'markers/(?P<pk>[0-9]+)/$', MarkerDetail.as_view(), name='marker-detail')

]
