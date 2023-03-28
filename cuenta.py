#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
# Construye los siguientes métodos para la clase:Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. 
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad):se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
# Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación
# que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:
#Un constructor.Los setters y getters para el nuevo atributo.
# En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad pero 
# menor de 25 años y falso en caso contrario.
# Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#Piensa los métodos heredados de la clase madre que hay que reescribir.
#



from pickle import FALSE, TRUE


class Cuenta():
    def __init__(self, nombre):
        self.titular = nombre 
        self.cant = 0
        
    def set_ingresar(self):
        self.cant = cantidad
        while True:
            ingreso = float(input(" \n Ingrese una cantidad: "))
            if ingreso <=0:
                print(" \n La cantidad ingresada debe ser mayor a 0 ")
            else:
                print(" \n La cantidad ingresada es: " ,ingreso)
            self.cant = self.cant + ingreso    
            x = input(" \n Desea seguir ingresando ? si / no: ")
            if x == "si":
                pass
            elif x == "no":
                break    
        print("\n El total ingresado es: ", self.cant)     
        
    def set_retirar(self):
        print("\n Usted tiene para retirar: $", self.cant)
        while True:
            retiro = float(input(" \n Ingrese una cantidad a retirar: "))
            if retiro <=0:
                print(" \n La cantidad para retirar debe ser mayor a 0 ")
            else:
                print(" \n La cantidad retirada  es: " ,retiro)
            self.cant = self.cant - retiro
            x = input("\n Desea seguir ingresando ? si / no: ")
            if x == "si":
                pass
                print(" \n Su cuenta tiene $" , self.cant)
            elif x == "no":
                print(" \n Su cuenta tiene $" , self.cant)
                break
            
    
    def get_mostrar_total(self):
        print(" \n Su total en cuenta es: $" , self.cant)
    
    def operar(self):
        while True:
            print(''' \n Ingreso a operacion:           #CAMBIAR ESTO POR UNA CTA COMUN NO JOVEN PARA GENTE + 25
            Opcion 1: Ingresar 
            Opcion 2: Retirar
            Opcion 3: Mostrar
            Opcion 4: Cerrar  
            \n ''')
            self.eleccion = int(input("\n Ingrese una opcion: "))
            if self.eleccion == 1:
                self.set_ingresar()
            if self.eleccion == 2:
                self.set_retirar()
            if self.eleccion == 3:
                self.get_mostrar_total()
            if self.eleccion == 4:
                print("Usted saldra del sistema.")
                break

######################################################## cuenta joven 

class Cuenta_Joven(Cuenta):
    def __init__(self, nombre, bonificacion = 0.10):
        super().__init__(nombre)
        self.h = bonificacion
        self.cantidad_joven = 0
        self.total = 0
        
    def esTitularValido(self):
        self.edad = TRUE
        while self.edad:
            self.age = int(input(" \n Ingrese su edad: "))
            if self.age <=25:
                return self.operar_joven()
            else:
                return self.operar()
            
    def set_ingresar_joven(self,bonificacion = 0.10):
        self.cantidad_joven = 0
        self.boni = bonificacion
        self.parcial = 0
        self.total = 0 
        while True:
            ingreso = float(input(" \n Ingrese una cantidad: "))
            if ingreso <=0:
                print(" \n La cantidad ingresada debe ser mayor a 0 ")
            else:
                print(" \n La cantidad ingresada es: $ " ,ingreso)
            self.cantidad_joven = self.cantidad_joven + ingreso
            x = input(" \n Desea seguir ingresando ? si / no: ")
            if x == "si":
                pass
            elif x == "no":
                break  
        self.parcial = self.cantidad_joven * bonificacion
        self.total = self.cantidad_joven + self.parcial  
        print("\n Tienes una bonificacion de: $  ", self.parcial)
        print("\n El total ingresado es de: $", self.total)        
    
    def set_retirar_joven(self):
        #self.total = 
        print("\n Usted tiene para retirar: $", self.total)
        while True:
            retiro = float(input(" \n Ingrese una cantidad a retirar: "))
            if retiro <=0:
                print(" \n La cantidad para retirar debe ser mayor a 0 ")
            else:
                print(" \n La cantidad retirada  es: " ,retiro)
            self.cantidad_joven = self.cantidad_joven - retiro
            x = input("\n Desea seguir ingresando ? si / no: ")
            if x == "si":
                pass
                print(" \n Su cuenta tiene $" , self.cantidad_joven)
            elif x == "no":
                print(" \n Su cuenta tiene $" , self.cantidad_joven)
                break
        
    
    
    def operar_joven(self):
        while True:
            print(''' \n  ----- Bienvenido a Cuenta Joven
                  Voce tendra una bonificacion del 10%  por ser nuevo cliente ----- \n      
                Ingreso a operacion:
            Opcion 1: Ingresar 
            Opcion 2: Retirar
            Opcion 3: Mostrar
            Opcion 4: Cerrar  
             ''')
            self.eleccion = int(input("\n Ingrese una opcion: "))
            if self.eleccion == 1:
                self.set_ingresar_joven()
            if self.eleccion == 2:
                self.set_retirar()
            if self.eleccion == 3:
                self.get_mostrar_total()
            if self.eleccion == 4:
                print("Usted saldra del sistema.")
                break            




nombre = input("Ingrese su nombre: ").title
cantidad = 0
bonificacion = 0.10
                        
juan = Cuenta_Joven(nombre)
juan.esTitularValido()
juan.operar() 
juan.operar_joven()
#juan.depositar()
#juan.extraer()
#juan.mostrar_total()