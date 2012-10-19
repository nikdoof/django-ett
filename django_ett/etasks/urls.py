from django.conf.urls import patterns, include, url

from .api import v1_api
from .views import TaskDetailView


urlpatterns = patterns('',
    url(r'^task/(?P<pk>.*)/$', TaskDetailView.as_view(), name='task-detail'),
    
    url('^api/', include(v1_api.urls)),
)
