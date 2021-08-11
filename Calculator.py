class Calculator:

    def Main():
        num1 = float(input("Número 1:"))
        num2 = float(input("Número 2: "))
        response = input("¿Qué operacion quiere hacer? ").lower()
        if(response == "suma"):
            print(Calculator.Sum(num1,num2))
        elif(response == "resta"):
            print(Calculator.Substract(num1,num2))
        elif(response == "multiplicacion"):
            Calculator.Multiply()
        elif(response == "division"):
            Calculator.Division()
        else:
            print("Respuesta inválida")

    @staticmethod
    def Sum(num1, num2):
        resultado = num1 + num2 
        return resultado

    @staticmethod
    def Substract(num1, num2):
        resultado = num1 - num2 
        return resultado

    @staticmethod
    def Multiply():
        pass

    @staticmethod
    def Division(x: float, y: float):
        pass

Calculator.Main()