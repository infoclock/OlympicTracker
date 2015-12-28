# encoding: utf-8
from django.conf.urls import patterns, url
from fileupload.views import (
	BasicVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = patterns('',
    url(r'^new/$', PictureCreateView.as_view(), name='upload-new'),
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
    url(r'^basic/$', BasicVersionCreateView.as_view(), name='upload-basic'),
)
