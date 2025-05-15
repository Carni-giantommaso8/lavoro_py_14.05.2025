def converti():
    valore = kg / conversione
    return round(valore, 2)

peso_totale = 0
limite_grammi = 9000

def menu():
    print("1 Inserisci un capo")
    print("2 Mostra il peso totale in kg")
    print("3 Mostra il peso convertito in libbre")
    print("4 Esci")

while True:
    menu()
    scelta = input("Scegli  ")

    if scelta == "1":
        try:
            peso = int(input("Inserisci il peso in grammi, 0 per annullare:  "))

            if peso < 0:
                print("riprova")
            elif peso == 0:
                print("riprova")
            elif peso_totale + peso > limite_grammi:
                print("riprova")
            else:
                peso_totale += peso
                print(f"Capo aggiunto. Peso attuale: {peso_totale / 1000} kg")
        except :
            print("riprova")

    elif scelta == "2":
        print(f"Peso totale dei capi inseriti: {peso_totale / 1000} kg")

    elif scelta == "3":
        kg = peso_totale / 1000
        libbre = converti(kg, 0.453592)
        print(f"Peso totale in libbre: {libbre} lb")

    elif scelta == "4":
        break

    else:
        print("Riprova")
