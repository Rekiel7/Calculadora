while True:
    print("                         ")
    print("_________________________")
    print("-------CALCULADORA-------")
    print("_________________________")

    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    print("5- Salir")
     

    try:
        print("ingrese a operacion a realizar: ")
   
        operacion = int(input())  

        if operacion == 5:
            break         

    except ValueError:
        print("ingrese un numero valido")
        operacion = False
        continue
  
    if operacion < 1 or operacion > 5:
        print("ingrese una opcion valida")
        operacion = False
        continue
        
        
    
    try:
        
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))


    except SyntaxError:
        print("ingrese un valor valido")
        operacion = False
    except ValueError:
        print("ingrese un numero valido")
        operacion = False
    
    if operacion:

        if operacion == 1:
            print("__________________")
            print("-------SUMA-------")
            print("__________________")

            suma=num1+num2
            print(f"La suma es: {suma}")
        elif operacion == 2:
            print("_________________")
            print("------Resta------")
            print("_________________")

            resta=num1-num2
            print(f"la resta es {resta}")
        elif operacion == 3:
            print("__________________")
            print("--Multiplicacion--")
            print("__________________")
            print('"operacion de multiplicacion"')
        elif operacion == 4:
            print("__________________")
            print("-----Division-----")
            print("__________________")
            print('"operacion de division"')
   


print("exited succesfuly")
        