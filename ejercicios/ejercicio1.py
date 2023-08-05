class Estudiante():
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"el estudiante {self.nombre} esta estudiando")


nombre = input("digame su nombre: ")
edad = int(input("digame su edad: "))
grado = int(input("digame su grado: "))

estudiante = Estudiante(nombre,edad,grado)

print(f'''
datos del estudiante:
      
nombre: {estudiante.nombre}
edad: {estudiante.edad}
grado: {estudiante.grado}

''')

estudiar = input()
if(estudiar == "estudiar"):
    estudiante.estudiar()