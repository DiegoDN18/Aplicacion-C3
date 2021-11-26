from rest_framework import serializers
from authApp.models.user import User
from authApp.models.pedido import Pedido
from authApp.serializers.pedidoSerializer import PedidoSerializer

class UserSerializer(serializers.ModelSerializer):
    pedido = PedidoSerializer()
    class Meta:
        model = User
#        fields = ['id', 'username', 'password', 'name', 'email', 'orden']
        fields = '__all__'
    # def create(self, validated_data):
    #     pedidoData = validated_data.pop('orden')
    #     userInstance = User.objects.create(**validated_data)
    #     Pedido.objects.create(user=userInstance, **pedidoData)
    #     return userInstance

    # def to_representation(self, obj):
    #     user = User.objects.get(id=obj.id)
    #     pedido = Pedido.objects.get(user=obj.id)       
    #     return {
    #                 'id': user.id,
    #                 'name': user.name,
    #                 'orden': {
    #                     'id': pedido.id,
    #                     'plato':pedido.suit,
    #                     'mesa':pedido.mesa
    #                 }
    #             }