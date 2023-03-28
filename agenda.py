class agenda():
    def __init__(self):
        self.contacto = []
           
    def menu(self):
        print('''Ingreso a gestión de cliente:
            Opcion 1: añadir contacto
            Opcion 2: Lista de contactos
            Opcion 3: Buscar contacto 
            Opcion 4: editar contacto
            Opcion 5: Cerrar agenda 
            ''')
        
    def elegir(self):   
        self.continuar = True
        while True:
            try:
                while self.continuar:
                    self.eleccion = int(input("ingrese una opcion: "))
                    if self.eleccion == 1:
                        self.añadir()
                    if self.eleccion == 2:
                        self.lista()
                    if self.eleccion == 3:
                        self.buscar()
                    if self.eleccion == 4:
                        self.editar()
                    if self.eleccion == 5:
                        self.cerrar()
                self.continuar = False
            except ValueError:
                print('\nSe ha producido un error, vuelva a intentarlo.')
                            
    def añadir(self):
        self.contacto = []
        print("Se creará el cliente")
        self.nombre = input("Ingrese su nombre: ")
        #self.contacto.append(self.nombre)
        self.telefono = int(input("Ingrese su telefono: "))
        #self.contacto.append(self.telefono)
        self.email = input("Ingrese su email: ")
        self.contacto.append(f"{self.nombre}, {self.telefono} , {self.email}")
             
    def lista(self):
        print("Mis contactos")
        if len(self.contacto) == 0:
            print("No hay contactos guardados")
        else:
            for x in self.contacto:
                print(x)
               
    def buscar(self):
        print("Buscar contacto")
        if len(self.contacto) > 0:
            serching = input("Ingrese nombre que desea buscar: ")
            for i in range(len(self.contacto)):
                print(i)
                if serching == self.contacto[i]:
                    print("Nombre:" ,self.nombre[i] )
                    print("Telefono: ",self.telefono[i])
                    print("Email: ", self.email[i])
                    return i
        else:
            print("No hay contacto ingreado aun")
    #def editar(self):
        
    #def cerrar(self):            
        
        
            
agendado = agenda()
agendado.menu()
agendado.elegir()
agendado.buscar()
agendado.editar