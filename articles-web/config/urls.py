from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from authy.views import user_profile

urlpatterns = [path('admin/', admin.site.urls),
               path('post/', include('post.urls')),
               path('account/', include('authy.urls')),
               path('ckeditor/', include('ckeditor_uploader.urls')),
               path('profile/<username>', user_profile, name='profile'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
