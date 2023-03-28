#Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
#La clase PlazoFijo tendrá dos atributos propios, plazo e interés. 
# Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información,
# datos del titular plazo, interés y total de interés. Crear al menos un objeto de cada subclase.


class Cuenta():
    def __init__(self, titular, cantidad):
        self.nombre = titular
        self.numero = cantidad
        
    #def imprimir(self):
    #    print("El titular de la cuenta es: ", self.nombre)
    #    print("La cantidad a depositar es:  ", self.numero)    
                              
    
class cajaahorro(Cuenta):
    def imprimir(self):
        print("El titular de la cuenta es: ", self.nombre)
        print("La cantidad a depositar es:  ", self.numero) 
        
class Plazofijo(Cuenta):
    def __init__(self, titular, cantidad, plazo):
        super().__init__(titular,cantidad)
        self._plazo = plazo
        self._interes = 0.60
        cajaahorro.imprimir(self)    
        
    def operacion(self):
        self.ganancia = self.numero*self._interes * self._plazo / 365
    
    def mostrar(self):
        print("Al sr/s: " , self.nombre , " \n Se le acreditarada de ganancia por depositar: " , self.numero , " \n un monto de: $ " , round(self.ganancia,2))        
        
        
titular = input("Ingrese su nombre: ").title
cantidad = int(input("Ingrese un monto a calcular: "))
plazo = int(input("Ingrese el plazo de dias: "))
#interes = int(input("Ingrese el interes: "))

tito = Plazofijo(titular,cantidad,plazo) 
#tito.imprimir()
tito.operacion()
tito.mostrar()

   
        
          