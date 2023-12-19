"""
crear un programa simple donde haya una jarra que se pueda llenar con maximo tres unidades de agua
y que se pueda vaciar completamente
"""

class Jarra():
    unid_agua = int
    llena = bool
    vacia = bool

    def iniciar(self):
        self.unid_agua = 0
        self.llena = False
        self.vacia = True

    def status(self):
        if self.unid_agua > 0 and self.unid_agua < 3 :
            print(f"status: La jarra tiene {self.unid_agua} unidades de agua")
        elif self.vacia:
            print("status: la jarra está vacía")
        elif self.llena:
            print("status: la jarra está llena")

    def llenar(self):
        if self.unid_agua < 3:
            self.unid_agua += 1
            self.vacia = False
            if self.unid_agua >= 3:
                self.llena = True
        else:
            print("aviso: la jarra ya está llena")

    def vaciar(self):
        if self.unid_agua > 0:
            self.unid_agua -= 1
            self.llena = False
            if self.unid_agua <= 0:
                self.vacia = True
        else:
            print("aviso: la jarra ya está vacía")

jarra = Jarra()
jarra.iniciar()

jarra.llenar()
jarra.llenar()
jarra.llenar()

jarra.status()

jarra.vaciar()
jarra.vaciar()
jarra.vaciar()
jarra.vaciar()

jarra.status()