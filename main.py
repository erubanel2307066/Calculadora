from sumar import sumar
from restar import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma Avanzada")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Ingrese su opción (1/2/3/4/5/6): ")

        if opcion == '6':
            print("Gracias por usar la calculadora. ¡Adiós!")
            break

        if opcion in ['1', '2', '3', '4']:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == '1':
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == '2':
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == '4':
                print(f"Resultado: {dividir(num1, num2)}")
        elif opcion == '5':
            nums = input("Ingrese los números a sumar separados por espacios: ")
            nums = list(map(float, nums.split()))
            print(f"Resultado: {suma_avanzada(*nums)}")
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
