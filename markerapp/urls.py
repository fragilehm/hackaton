from django.conf.urls import url

from .views import CategoryList, MarkerListByCategoryID, MarkerDetail, NeedMarkerListByCategoryID, \
    WantMarkerListByCategoryID


urlpatterns = [
    url(r'^categories/$', CategoryList.as_view(), name='category-list'),
    url(r'^categories/(?P<pk>[0-9]+)/$', MarkerListByCategoryID.as_view(), name='marker-list-by-category-id'),
    url(r'^need/categories/(?P<pk>[0-9]+)/$', NeedMarkerListByCategoryID.as_view(), name='need-marker-list-by-category-id'),
    url(r'^want/categories/(?P<pk>[0-9]+)/$', WantMarkerListByCategoryID.as_view(), name='want-marker-list-by-category-id'),
    # url(r'categories/(?P<pk>[0-9]+)/$', MarkerListBySeveralCategoryID.as_view(), name='marker-list-by-several-category-id'),
    url(r'markers/(?P<pk>[0-9]+)/$', MarkerDetail.as_view(), name='marker-detail')

]
