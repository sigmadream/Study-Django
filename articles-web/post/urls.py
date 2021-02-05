from django.urls import path
from post.views import index
from django.views.generic import TemplateView

urlpatterns = [
    path('hello/', index, name='hello'),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
]
