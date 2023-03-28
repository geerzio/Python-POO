#En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
# El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
# Se deberán crear dos clases, la clase cliente y la clase banco. 
# La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
#La clase banco tendrá los atributos de la clase cliente y los métodos __init__, operar y deposito_total.


class Cliente():
    def __init__(self, nombre ,cantidad):
        self.nombre = nombre
        self.cantidad = cantidad 
        
    def depositar(self):
        #self.seguir = False
        
        while True:
            self.deposito = int(input("Ingrewse cuanto dinero quiere depositar: "))
            self.x = input("Desea seguir depositando ? si / no: ")
            if self.x == "si":
                pass
            if self.x == "no":
                break  
        self.depositacion = self.deposito + self.deposito
        
    def extraer(self):
        #self.seguir = False
        
        while  True:
            self.extraccion = int(input("Cuanto dinero desea extraer ?: "))
            self.x = input("Desea seguir extrayendo  ? si / no: ")
            if self.x == "si":
                pass
            if self.x == "no":
                break
        self.retiro = self.extraccion + self.extraccion     
    
    def mostrar_total(self):
        print("Usted a depositado: " , self.depositacion)
        print("Usted a extraido: " , self.retiro)

class Banco(Cliente):
    
    def operar(self):
        print('''Ingreso a operacion de banco:
            Opcion 1: Deposit
            Opcion 2: Extraccion
            Opcion 3: Mostrar
            Opcion 4: Cerrar  
            ''')
        while True:
            self.eleccion = int(input("Ingrese una opcion: "))
            if self.eleccion == 1:
                self.depositar()
            if self.eleccion == 2:
                self.extraer()
            if self.eleccion == 3:
                self.mostrar_total()
            if self.eleccion == 4:    
                break                          
    
    #def deposito_total(self):
    #    print("El deposito total del banco es de: $ ") 
               
nombre = input("Ingrese su nombre: ")
cantidad = int(input("Ingrese una cantidad $ : "))               
                    
juan = Banco(nombre,cantidad)
juan.operar() 
#juan.depositar()
#juan.extraer()
juan.mostrar_total()
#juan.deposito_total()

           
        
        
            
        
             