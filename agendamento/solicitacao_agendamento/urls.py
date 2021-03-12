from django.urls import path, include
from rest_framework import routers
from .views import ComunicadoViewSet, EnvioComunidadoView, ConsultaComunidadoView, deletaComunicado
from django.conf.urls import url, include
from rest_framework import permissions, authentication

app_name = 'solicitacao_agendamento'


router = routers.DefaultRouter()
router.register(r'solicitacao_agendamento', ComunicadoViewSet)

urlpatterns = [

    path('api/', include(router.urls)),
    path('api/envio/', EnvioComunidadoView.as_view() , name="envio_comunicado"), #endpoint1 cadastrar comunicado
    path('api/consulta/<int:pk>/', ConsultaComunidadoView.as_view() , name="consulta_comunicado"), #endpoint2 consultar comunicado
    path('api/deleta/<int:pk>/', deletaComunicado , name="deleta_comunicado"), #endpoint3 deletar comunicado
]
