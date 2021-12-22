pin = 1234
balance = 997

def decision():
    global balance
    print ("Co chcesz zrobić w kolejnym kroku?")
    print ("Sprawdź saldo -> wybierz 1")
    print ("Wpłata -> wybierz 2")
    print ("Wypłata -> wybierz 3")
    print ("Zakończ -> wybierz 4")
    action = int(input())

    if action == 4:
        print ("Do widzenia!")
        exit()

    elif action == 1:
        your_pin = int(input("Podaj PIN: "))
        if your_pin == pin:
            print (f'Twoje saldo wynosi {balance} PLN\n')
        else:
            print ("Błędny PIN\n")
        decision()

    elif action == 2:
        your_pin = int(input("Podaj PIN: "))
        if your_pin == pin:
            transfer = int(input("Wprowadź kwotę, którą chcesz wpłacić: "))
            balance += transfer
            print(f"Wpłaciłeś {transfer} PLN\n")
        else:
            print ("Błędny PIN\n")
        decision()

    elif action == 3:
        your_pin = int(input("Podaj PIN: "))
        if your_pin == pin:
            transfer = int(input("Wprowadź kwotę, którą chcesz wypłacić: "))
            if transfer <= balance:
                balance -= transfer
                print(f"Wypłaciłeś {transfer} PLN\n")
            else:
                print ("Brak wystarczającej liczby środków na koncie\n")
                decision()
        else:
            print ("Błędny PIN\n")
        decision()

    else:
        print ("Błąd wyboru\n")
        decision()

decision()
