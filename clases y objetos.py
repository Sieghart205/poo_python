class Celular():
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def mostrarData(self):
        print(f"tienes un {self.marca}, modelo {self.modelo}, con una camara de {self.camara}")


celular1 = Celular("Samsung","S23","48MP")
celular2 = Celular("Apple","Iphone 15","96MP")

celular1.mostrarData()