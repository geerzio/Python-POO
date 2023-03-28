# Cree la clase Persona, el método estático mostrarPersona(), que devuelve aleatoriamente una de las 
# cadenas de piedra, papel o tijera; cree la clase Computadora, el método de clase mostrarCompu(),
# Devuelve aleatoriamente uno de los resultados: de piedra, papel, tijera; crea la clase Game, 
# los atributos de clase del objeto Persona y el objeto Computadora, y el método de clase startGame() / ComenzarJuego().
# Imprime el puntaje, muestra si la computadora gana o la persona gana.


import random

#choice = input(" Piedra, papel o tijera ?: ")

#choice = input(" Piedra, papel o tijera ?: ")

class Persona(object):
    def __init__(self,nombre):
        self.name = nombre
        print(self.name)
        
    #def mostrarPersona(self):
    #    self.elige = input( self.name , "Que eliges ?  Piedra, papel o tijera: ")
    

class Computadora(object):
    def MostrarCompu(self):
        self.verdad = random.choice(["piedra","papel","tijera"])
        return self.verdad 
          
class game(Persona,Computadora):
        #self.verdad = random.choice[("piedra","papel","tijera")]
        #self.nombre = nombre
    def stargame(self):
        self.player = 0
        self.pc = 0
        #print('''Ingrese una opcion:
        #    Opcion 1: Play 
        #    Opcion 2: Exit
         #   ''')
        while True:
            print(''' \n Ingrese una opcion:
            Opcion 1: Play 
            Opcion 2: Exit
            ''')
            self.eleccion = int(input("Ingrese una opcion: "))
            if self.eleccion == 1:
                while True:
                    self.elige = input( "Que eliges ? Piedra, papel o tijera ?: ")
                    self.verdad = Computadora.MostrarCompu(self)
                    print("El ordenador ha elegido" , self.verdad)
                    if self.elige == "piedra" and self.verdad == "piedra":   
                        print("Es un empate!")
                    elif self.elige == "tijera" and self.verdad == "tijera":
                        print("Es un empate!")
                    elif self.elige == "papel" and self.verdad == "papel":
                        print("Es un empate!")    
                    elif self.elige == "piedra" and self.verdad == "tijera":
                        print("Ha ganado player 1")
                        self.player +=1
                    elif self.elige == "papel" and self.verdad == "piedra":
                        print("Ha ganado player 1")
                        self.player +=1
                    elif self.elige == "tijera" and self.verdad == "papel":
                        print("Ha ganado" , self.name)
                        self.player +=1
                    else:
                        print("Ha ganado el ordenar")
                        self.pc +=1
                    print (self.name,  "tiene: ", self.player , "puntos" "\n y el ordenador tiene:" , self.pc)                   
                    self.x = input("Quieres seguir jugando? (si/no) ")
                    if self.x == "si":
                        True
                    elif self.x == "no":
                        print("\n Gracias por jugar !  ")
                        break
            if self.eleccion == 2:
                print("BYE")
                break

nombre = input("Ingrese nombre: ").title()

jugador1 = game(nombre)
#jugador1.MostrarCompu()
jugador1.stargame()
#jugador1.MostrarCompu()
    
    
    

       
    