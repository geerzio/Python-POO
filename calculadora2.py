class calculadora():
    def __init__(self):
        while self.ingreso1 and self.ingreso2 and self.caracter:
            self.ingreso1 = int(input("Ingrese un segundo numero: "))    
            self.ingreso2 = int(input("Ingrese un segundo numero: "))
            self.resultado = 0
            self.caracter = input("Ingrese el caracter para realizar la operatoria, ej. + , * , / , - : ")
    
    def get_suma(self): # suma
        self.suma = self.ingreso1 + self.ingreso2
        #print(f"{self.ingreso1} + {self.ingreso2} = {self.suma}")
    
    def get_resta(self): # suma
        self.resta = self.ingreso1 - self.ingreso2
        #print(f"{self.ingreso1} - {self.ingreso2} = {self.resta}")   

    def get_multiplicacion(self): # suma
        self.multiplicacion = self.ingreso1 * self.ingreso2
        #print(f"{self.ingreso1} * {self.ingreso2} = {self.multiplicacion}")

    def get_division(self): # suma
        self.division = self.ingreso1 / self.ingreso2
        #print(f"{self.ingreso1} / {self.ingreso2} = {self.division}")   
    def operacion(self):
        if self.caracter == "/":
            self.get_division()
            print(f"{self.ingreso1} / {self.ingreso2} = {self.division}")
        elif self.caracter == "+":
            self.get_suma()
            print(f"{self.ingreso1} + {self.ingreso2} = {self.suma}")
        elif self.caracter == "-":
            print(f"{self.ingreso1} - {self.ingreso2} = {self.resta}")
        else:
            self.caracter == "*"
            print(f"{self.ingreso1} * {self.ingreso2} = {self.multiplicacion}")
                
                               



calculator = calculadora()
calculator.get_suma()
calculator.get_resta()
calculator.get_multiplicacion()
calculator.get_division()
calculator.operacion()
calculator.self