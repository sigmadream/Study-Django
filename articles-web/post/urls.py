from django.urls import path
from .views import index, category, tags, post_details, contact, contact_success

urlpatterns = [
    path('', index, name='index'),
    path('categories/<slug:category_slug>', category, name='categories'),
    path('tags/<slug:tag_slug>', tags, name='tags'),
    path('<slug:post_slug>', post_details, name='article-details'),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact-success')
]
