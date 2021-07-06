from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
