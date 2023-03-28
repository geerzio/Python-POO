#Botella y Sacacorchos:
#a) Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega). 
#b) Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está destapada
#c) Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, 
# o si el sacacorchos ya contiene un corcho.
#d) Agregar un método limpiar, que saque el corcho del sacacorchos, o 
# lance una excepción en el caso en el que no haya un corcho.


from operator import truediv


class corcho(object):
    def __init__(self,bodega):
        self.name = bodega

    def mostrar(self):
        print("El nombres de la bodega: " , self.name)    

class botella():
    def corcho(self):
        self.tapada = True
        #return "\n La botella esta tapada y sera destapada"
    def destapada(self):    
        self.destapada = None
        return "\n La botella esta destapada"
        
class sacacorchos(botella, corcho):
    def destapar(self):
        self.destapacion = input("Deseea sacar el corcho: si/no ?:  ")
        if self.destapacion == "si":
            self.tapada = False
            print("La botella esta tapada y sera destapada") 
        elif self.destapacion == "no":
            raise AttributeError(" La botella ya esta destapada \n El sacacorcho ya contiene un corcho")               
        
    def limpiar(self):
        self.limpia = input("\n Desea sacar el corcho del sacacorcho ? : ")
        if self.limpia == "si":
            self.destapada = True
            print(" El corcho sera removido del sacacorcho")
        elif self.limpia == "no":
            self.tapada = True
            print("La botella aun sigue tapada")    
            
        
           


vino = sacacorchos(" BODEGA el 14 ")
#print(vino.corcho(True))
#print(vino.destapada())
#vino.mostrar()
vino.mostrar()
vino.corcho()
vino.destapada()
vino.destapar()
vino.limpiar()


#raise AttributeError("La botella ya esta destapada")
        
'''''   
class corcho(object):
    def _init_(self , bodega = ""):
        self.name = bodega

    def mostrar(self):
        print(self.name)    

class botella(corcho):
    def _init_(self, corcho):
        self.corcho = corcho
    

vino = botella("El 14 ")
vino.mostrar()   
'''''