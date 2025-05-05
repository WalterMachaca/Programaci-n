def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos"
    elif n == 0:
        return 1
    else:
        resultado= 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
           
def main():
    try:
        n = int(input("Ingrese un número entero positivo: "))
        print(f"El factorial de {n} es: {factorial(n)}") 
    except ValueError:
        print("Por favor, ingrese un número entero positivo válido.")  
if __name__ == "__main__":
    main()  
    
 

        