from django.conf.urls import url
from ProblemApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^setor$', views.setorApi),
    url(r'^setor/([0-9]+)$', views.setorApi),

    url(r'^website$', views.websiteApi),
    url(r'^website/([0-9]+)$', views.websiteApi),

    url(r'^usuario$', views.usuarioApi),

    #Salva as imagens (logo dos sites)
    url(r'^website/salvararquivo', views.SalvarArquivo)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)