class Animal:
    def comer(self):
        print("el animal esta comiendo")


class Mamifero:
    def amamantar(self):
        print("el mamifero alimenta a su cria")

class Ave:
    def volar(self):
        print("el ave esta volando")

class Murcielago (Mamifero,Ave):

    def amamantar(self):
        print("el murcielago alimenta a su cria")

    def volar(self):
        print("el murcielago esta volando")

    def comer(self):
        print("el murcielago come")

animal = Animal()
animal.comer()

ave = Ave()
ave.volar()

murcielago = Murcielago()
murcielago.amamantar()
murcielago.volar()
murcielago.comer()

print(Murcielago.mro())