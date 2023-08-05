class A():
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")


d = D()

d.hablar()