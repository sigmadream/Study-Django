from django.urls import path
from .views import index, category, tags, post_details

urlpatterns = [
    path('', index),
    path('categories/<slug:category_slug>', category, name='categories'),
    path('tags/<slug:tag_slug>', tags, name='tags'),
    path('<slug:post_slug>', post_details, name='article-details')
]
