from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^$', TemplateView.as_view(template_name='pony/pony.html')),
)
