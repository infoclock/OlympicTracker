# encoding: utf-8
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


from fileupload.views import (
		BasicVersionCreateView,
        SubmissionCreateView, SubmissionDeleteView, SubmissionListView,
        SubmitList,
)

urlpatterns = patterns('',
    url(r'^view/$', permission_required('is_staff')(SubmissionListView.as_view()), name='upload-view'),
    url(r'^basic/$', permission_required('is_staff')(BasicVersionCreateView.as_view()), name='upload-basic'),
)
