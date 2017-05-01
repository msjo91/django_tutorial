from django.conf.urls import url

from .views import cbv, fbv

app_name = 'polls'
urlpatterns = [
    url(r'^$', cbv.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', cbv.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', cbv.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', fbv.vote, name='vote'),
]
