from django.db import models 
from .user import User 
 
class Pedido(models.Model): 
    id = models.AutoField(primary_key=True) 
#    user = models.ForeignKey(User, related_name='orden', on_delete=models.CASCADE) 
    platos=(
        ("churrasco","Churrasco"),
        ("pollo","Pollo"),
        ("pescado","Pescado"),
        ("camarones","Camarones")
    )
    platos = models.CharField(max_length=10, choices=platos, default="pollo")
    cliente = models.CharField(max_length=100)
    precio = models.IntegerField()
    mesa = models.IntegerField()
    anotacion = models.CharField(max_length=100,default="ninguna")
#    balance = models.IntegerField(default=0) 
#    lastChangeDate = models.DateTimeField() 
#    isActive = models.BooleanField(default=True) 