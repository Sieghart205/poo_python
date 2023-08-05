class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("holi")


class Estudiante(Persona):
    def __init__(self,nombre,edad,nacionalidad,curso):
        super().__init__(nombre,edad,nacionalidad)
        self.curso = curso

    def hablar(self):
        print(f"hola, me llamo {self.nombre}, estoy estudiando {self.curso}")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo = trabajo
        self.salario = salario

    def hablar(self):
        print(f"Hola, me llamo {self.nombre}, soy un {self.trabajo}")


persona = Persona("Sol",47,"Colombiana")
persona.hablar()


empleado = Empleado("Fabian",40,"Colombiano","Ingeniero industrial",4000000)
empleado.hablar()

estudiante = Estudiante("jeisson",16,"Colombiano","diseño e integracion de contenidos digitales")
estudiante.hablar()