from django.db import models



# Create your models here.
class Comunicado(models.Model):
    tipoChoices= ((0,"E-mail"),(1, "SMS"),(2, "Push"),(3, "WhatsApp"))
    statusChoices=((0,"Não Enviado"),(1, "Enviado"))

    data_hora = models.DateTimeField()
    destinatario = models.CharField(max_length=100)
    mensagem = models.CharField(max_length=200)
    tipo =  models.IntegerField(default=0,choices=tipoChoices)
    status_envio =  models.IntegerField(default=0,choices=statusChoices)

    class Meta:
        ordering = ['data_hora']
        db_table = 'solicitacao_agendamento_comunicado'

    @classmethod
    def create(cls, data_hora, destinatario, mensagem, tipo, status_envio):
        comunicado = cls(data_hora=data_hora, destinatario=destinatario,mensagem=mensagem,tipo=tipo,status_envio=status_envio)
        return comunicado

    objects = models.Manager()
