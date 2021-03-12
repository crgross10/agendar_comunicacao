from django.shortcuts import render
from rest_framework import viewsets
from .models import Comunicado
from .serializer import ComunicadoSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import json
from datetime import date, datetime
from rest_framework.decorators import api_view

# Create your views here.
class ComunicadoViewSet(viewsets.ModelViewSet):
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSerializer



class EnvioComunidadoView(APIView):
    parser_class = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        print('entrou')
        retorno = self.request.data
        print('passou')
        data_hora = retorno.get('data_hora')
        destinatario = retorno.get('destinatario')
        mensagem  = retorno.get('mensagem')
        tipo = retorno.get('tipo')
        status_envio = retorno.get('status_envio')
        comunicado = Comunicado.create(data_hora, destinatario, mensagem, tipo, status_envio)
        comunicado.save()

        msg = 'Comunicado agendado!'

        return Response({'status': msg})


class ConsultaComunidadoView(APIView):
    parser_class = [MultiPartParser]

    def get(self, request, pk, format=None):
        try:
            comunicado = Comunicado.objects.filter(id=pk)

            for c in comunicado:
                data_hora = datetime.strftime(c.data_hora,"%d/%m/%Y %H:%M:%S")
                if c.tipo == 0:
                    tipo = 'E-mail'
                elif c.tipo == 1:
                    tipo = 'SMS'
                elif c.tipo == 2:
                    tipo = 'Push'
                else:
                    tipo ='WhatsApp'

                if c.status_envio == 0:
                    status_envio = 'NÃO ENVIADO'
                else:
                    status_envio ='ENVIADO'

        #    dth = datetime.strptime(str(data_hora),'%Y-%m-%d %H:%M:%S'  )

            msg = 'O comunicado agendado para ' + str(data_hora) + ' do tipo ' + tipo +' está com status de ' + status_envio + '.'
        except:
            msg='Comunicado não encotrado ou não cadastrado!'

        return Response({'status': msg})





@api_view(['DELETE'])
def deletaComunicado(self, pk, format=None):
        comunicado = Comunicado.objects.filter(id=pk)
        if len(comunicado)>0:
            comunicado.delete()
            msg = 'O comunicado foi deletado com sucesso!'
        else:
            msg='Comunicado não encotrado ou não cadastrado!'

        return Response({'status': msg})
