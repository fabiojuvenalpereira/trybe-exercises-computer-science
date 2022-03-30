from datetime import datetime
from random import randint

def gerar_num_pedido():
    return randint(0,100)

def gerar_horario_pedido():
    data = datetime.now()
    parsed = data.strftime("%d/%m/%Y %H:%M")
    return parsed

class Order:
    def __init__(self, order, cliente, atendente):
        self.order = order
        self.cliente = cliente
        self.atendente = atendente
        self.horario = gerar_horario_pedido()
        self.num_pedido = gerar_num_pedido()

    def order(self):
        return self.order

    def cliente(self):
        return self.cliente

    def atendente(self):
        return self.atendente

    def horario(self):
        return self.horario

    def calcula_preco(self):
        items = self.order
        total = 0

        for item in items:
            total += item["unit_price"] * item["quantity"]
        return total

    def complete_order(self):
        return f" pedido: {self.num_pedido} \n\n nome do cliente: {self.cliente} \n\n data e hora do pedido: {self.horario} \n\n total do pedido: R$ {self.calcula_preco()}"





new_order = [
    {"name": "café", "quantity": 1, "unit_price": 1.20},
    {"name": "pão", "quantity": 1, "unit_price": 1.50},
    {"name": "mamão", "quantity": 1, "unit_price": 0.70},
    {"name": "ovo", "quantity": 1, "unit_price": 1.00}
]
generate_order = Order(new_order, "joaozinho", "marina")

print(generate_order.complete_order())