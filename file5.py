def converti():
    valore = kg / conversione
    return round(valore, 2)

def calcola_costo():
    if (temp != 40) and (temp != 60) and (temp != 90):
        return -1  
    elif peso_kg < 0:
        return -1  

    if peso_kg < 5:
        if temp == 40:
            costo = peso_kg * 0.50
        elif temp == 60:
            costo = peso_kg * 0.75
        else:  
            costo = peso_kg * 1.00
    elif peso_kg >= 5:
        if temp == 40:
            costo = peso_kg * 0.75
        elif temp == 60:
            costo = peso_kg * 1.00
        else: 
            costo = peso_kg * 1.50

peso_totale = 0
limite_grammi = 9000

def menu():
    print("1 Inserisci un capo")
    print("2 Mostra il peso totale in kg")
    print("3 Mostra il peso convertito in libbre")
    print("4 Esci")
    print("5 Calcola il costo")

while True:
    menu()
    scelta = input("Scegli :  ")

    if scelta == "1":

            peso = int(input("Inserisci il peso in grammi, 0 per annullare: "))
            if peso < 0:
                print("riprova")
            if peso == 0:
                print("riprova")
            if peso_totale + peso > limite_grammi:
                print("riprova")
            else:
                peso_totale += peso
                print(f"Capo aggiunto. Peso attuale: {peso_totale / 1000} kg")

    if scelta == "2":
        print(f"Peso totale dei capi inseriti: {peso_totale / 1000} kg")

    if scelta == "3":
        kg = peso_totale / 1000
        libbre = converti(kg, 0.453592)
        print(f"Peso totale in libbre: {libbre} lb")

    if scelta == "4":
        break

    if scelta == "5":
        kg = peso_totale / 1000
        try:
            temp = int(input("Inserisci la temp di lavaggio 40 o 60 o 90: "))
            costo = calcola_costo(kg, temp)
            if costo == -1:
                print("riprova")
            else:
                print(f"Il costo del lavaggio è: {costo}")
        except ValueError:
            print("riprova con (40, 60, 90).")

    else:
        print("Riprova")
