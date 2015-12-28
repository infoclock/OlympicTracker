# encoding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from fileupload.views import (
	BasicVersionCreateView,
        PictureCreateView, PictureDeleteView, PictureListView,
        )

urlpatterns = patterns('',
    url(r'^delete/(?P<pk>\d+)$', PictureDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', PictureListView.as_view(), name='upload-view'),
    url(r'^basic/$', login_required(BasicVersionCreateView.as_view()), name='upload-basic'),
)
