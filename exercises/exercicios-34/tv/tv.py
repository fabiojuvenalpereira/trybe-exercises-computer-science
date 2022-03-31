class Tv:
    def __init__(self, tamanho):
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume < 100 and self.__volume < 0:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume < 100 and self.__volume < 0:
            self.__volume -= 1

    def modificar_canal(self, canal):
        if  0 < canal < 100:
            self.__canal = canal
        else:
            raise ValueError("Canal Não existente")

    def ligar_desligar(self):
        self.__ligada = not self.__ligada

new_tv = Tv(32)
print(new_tv.ligar_desligar())