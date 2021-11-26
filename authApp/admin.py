from django.contrib import admin
from .models.user import User
from .models.pedido import Pedido

admin.site.register(User)
admin.site.register(Pedido)

