from django.conf.urls import url
from . import views

urlpatterns = [
  # post views
  url(r'^$', views.post_list, name='posts_list'),
  # post detail view
  url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
      views.post_detail,
      name='post_detail'),
  url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]