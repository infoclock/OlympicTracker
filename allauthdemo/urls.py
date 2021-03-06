from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import permission_required

from . import views
import allauthdemo.views
from allauthdemo.demo.views import ProblemView, SubmissionView, RankingView, ParticipantView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),

    url(r'^problem-list$', ProblemView.as_view(), name='problem_list'),
    url(r'^submission-list$', SubmissionView.as_view(), name='submission'),
    url(r'^ranking$', RankingView.as_view(), name='ranking'),
    url(r'^participant/(?P<user_id>[0-9]+)/$', ParticipantView.as_view(), name='participant'),

    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),

    (r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'allauthdemo.auth.views.account_profile', name='account_profile'),

    url(r'^member/$', allauthdemo.views.member_index, name='user_home'),
    url(r'^member/action$', allauthdemo.views.member_action, name='user_action'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^upload/', include('fileupload.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


from os.path import join, abspath, dirname
urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': join(abspath(dirname(__file__)), 'media')}),
)
