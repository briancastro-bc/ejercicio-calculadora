class Calculator:

    def Main():
        num1 = float(input("Número 1:"))
        num2 = float(input("Número 2: "))
        response = input("¿Qué operacion quiere hacer? ").lower()
        if(response == "suma"):
            Calculator.Sum()
        elif(response == "resta"):
            Calculator.Substract()
        elif(response == "multiplicacion"):
            Calculator.Multiply()
        elif(response == "division"):
            Calculator.Division()
        else:
            print("Respuesta inválida")

    @staticmethod
    def Sum(x: float, y: float):
        pass

    @staticmethod
    def Substract(x: float, y: float):
        pass

    @staticmethod
    def Multiply():
        pass

    @staticmethod
    def Division(x: float, y: float):
        pass