import os
class Calculadora:
    def __init__(self, v1, v2):
        self .v1 = v1
        self .v2 = v2

    def suma(self):
        if self.v2 < 0:
            return "La Suma de {}-{} ({}+{}) es igual a {}".format(self.v1, -self.v2, self.v1, self.v2, self.v1 + self.v2)
        else:
            return "La Suma de {}+{} es igual a {}".format(self.v1, self.v2, self.v1 + self.v2)

    def resta(self):
        if self.v2 < 0:
            return "La Resta de {}+{} ({}-{}) es igual a {}".format(self.v1, -self.v2, self.v1, self.v2, self.v1 - self.v2)
        else:
            return "La Resta de {}-{} es igual a {}".format(self.v1, self.v2, self.v1 - self.v2)

    def multiplicar(self):
        if (self.v1 * self.v2 == -0.0) and (self.v1 < 0 or self.v2 < 0):
            return "La Multiplicacion de {}*{} es igual a {}".format(self.v1, self.v2, -(self.v1 * self.v2))
        else:
            return "La Multiplicacion de {}*{} es igual a {}".format(self.v1, self.v2, self.v1 * self.v2)

    def division(self):
        if (self.v1 / self.v2 == -0.0) and (self.v1 < 0 or self.v2 < 0):
            return "La Division de {}/{} es igual a {}".format(self.v1, self.v2, -(self.v1 / self.v2))
        elif self.v2 == 0:
            return "No se pueden realizar divisiones entre cero ({}/{})".format(self.v1, self.v2)
        elif self.v1 == 0 and self.v2 < 0:
            self.v2 = int(self.v2)
            return "La Division de {}/{} es igual a {}".format(self.v1, self.v2, -(self.v1 / self.v2))
        else:
            return "La Division de {}/{} es igual a {}".format(self.v1, self.v2, self.v1 / self.v2)

    def potencia(self):
        if self.v2 < 0:
            return "El resultado de la potencia negativa {}^{} es  1/{} o {}".format(self.v1, self.v2, self.v1**-self.v2, self.v1**self.v2)
        elif self.v2 == 0:
            return "Todo numero elevado a la 0 es igual a 1 ({}^{})".format(self.v1, self.v2)
        else:
            return "La Potencia de {}^{} es igual a {}".format(self.v1, self.v2, self.v1**self.v2)

    def raiz_cuadrada(self):
        if self.v1 < 0 and self.v2 % 2 == 0:
            return "No se pueden realizar raices pares de numeros negativos ({}√{})".format(self.v2, self.v1)
        elif self.v1 < 0 and self.v2 % 2 != 0:
            self.v1 = -self.v1
            self.v1 = int(self.v1)
            return "La Raiz impar ({}) del numero negativo {} ({}√{}) es igual a {}".format(self.v2, -self.v1, self.v2, -self.v1, -(self.v1 ** (1 / self.v2)))
        elif self.v2 == 0:
            return "No se pueden realizar raices a la 0 ({}√{})".format(self.v2, self.v1)
        elif self.v2 < 0:
            self.v2 = -self.v2
            self.v2 = int(self.v2)
            return "La Raiz negativa de {}√{} es igual a 1/{} o {}".format(-self.v2, self.v1, self.v1**(1/self.v2), 1/(self.v1**(1/self.v2)))
        else:
            return "La Raiz de {}√{} es igual a {}".format(self.v2, self.v1, self.v1**(1/self.v2))



if __name__=="__main__":
    while True:
        print("Bienvenido(a)")
        print("\nOPCIONES")
        print("1.Suma")
        print("2.Resta")
        print("3.Multiplicacion")
        print("4. Division")
        print("5. Potencia")
        print("6.Raiz cuadrada")
        print("7. Salir")
        opcion = int(input("Elige lo que deseas hacer: "))

        if opcion ==7:
            print("GRACIAS POR PREFERISNOS")
            print("ADIOS")
            break
        elif opcion == 1:

            v1 = float(input("Inserta un Numero :"))
            v2= float(input("Mas (otro Numero) : "))
            operacion = Calculadora(v1, v2)
            print(operacion.suma())

        elif opcion == 2:
            v1= int(input("Inserta un Numero :"))
            v2= int(input("Menos (otro Numero) : "))
            operacion = Calculadora(v1,v2)
            print(operacion.resta())

        elif opcion == 3:
            v1= int(input("Inserta un Numero :"))
            v2= int(input("Por (otro Numero) : "))
            operacion = Calculadora(v1,v2)
            print(operacion.multiplicar())
        elif opcion == 4:
            v1= int(input("Inserta un Numero :"))
            v2= int(input("Entre (otro Numero) : "))
            operacion = Calculadora(v1,v2)
            print(operacion.division())
        elif opcion == 5:
            v1= int(input("Inserta un Numero :"))
            v2= int(input("Potenciado por(otro numero) : "))
            operacion = Calculadora(v1,v2)
            print(operacion.potencia())
        elif opcion == 6:
            v1 = int(input("El numero que desea radicar (numero):"))
            v2 = int(input("El tipo de raiz (otro numero) : "))
            operacion = Calculadora(v1, v2)
            print(operacion.raiz_cuadrada())

            break
        else:
            print("Opcion Invalida, Intente nuevamente")
        while True:
            continuar = input("Desea seguir en utilizando la calculadora? (S/N): ")
            if continuar.lower() == "n" or continuar.lower() == "no":
                print("GRACIAS POR PREFERISNOS")
                print("ADIOS")
                exit()
            elif continuar.lower() == "s" or continuar.lower() == "si":
                break
            else:
                print("Seleccion Invalida, Intente nuevamente")