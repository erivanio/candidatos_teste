from django.conf.urls import patterns, url
from apps.core.views import CandidateCreateView

urlpatterns = patterns('',
    url(r'^$', CandidateCreateView.as_view(), name='candidate_register')
)
