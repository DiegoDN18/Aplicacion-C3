from authApp.models.pedido import Pedido
from rest_framework import serializers

class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
#        fields = ['platos','mesa']
        fields = '__all__'