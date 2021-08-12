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
            print(Calculator.Multiply(num1,num2))
        elif(response == "division"):
            print(Calculator.Division(num1,num2))
        else:
            print("Respuesta inválida")

    @staticmethod
    def Sum(x: float, y: float):
        pass

    @staticmethod
    def Substract(x: float, y: float):
        pass

    @staticmethod
    def Multiply(x: float, y: float):
        resultado = x * y
        return resultado

    @staticmethod
    def Division(x: float, y: float):
        resultado = x / y
        return resultado

Calculator.Main()