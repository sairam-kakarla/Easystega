from django.urls import path
from .views import  encode,decode,about_us
from django.conf import settings
from django.conf.urls.static import static
app_name='menu'
urlpatterns = [
    path('encode',encode,name="encode"),
    path('decode',decode,name="decode"),
    path('about_us',about_us,name="about_us"),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)