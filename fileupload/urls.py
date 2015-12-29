# encoding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from fileupload.views import (
		BasicVersionCreateView,
        SubmissionCreateView, SubmissionDeleteView, SubmissionListView,
        SubmitList,
)

urlpatterns = patterns('',
    url(r'^view/$', login_required(SubmissionListView.as_view()), name='upload-view'),
    url(r'^basic/$', login_required(BasicVersionCreateView.as_view()), name='upload-basic'),
)
