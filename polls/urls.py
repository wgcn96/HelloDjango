from django.conf.urls import url
from . import views

app_name = 'polls'  #URL_config  命名空间
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    # es: /polls/specifics/5/
    url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]