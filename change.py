def change():
    expense = 23.75
    money = 100
    vuelto= money - expense
    print("Ingresar gasto:") 
    print(expense)
    print("dinero recibido")
    print(money)
    print("\nvuelto")
    print("\npesos:")
    print(int(vuelto))
    print("centavos:")
    print(int((vuelto - int(vuelto))*100))
change()
