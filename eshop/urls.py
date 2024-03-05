from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
# from django.conf import settings
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include('blog.urls')),
    path('account/', include('account.urls')),
    path('', views.home, name="home"),
    # testing urls
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
