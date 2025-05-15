PESO_MASSIMO_KG = 9
peso_totale_kg = 0

def menu():
    print("Il peso massimo consentito è 9 kg.")
    print("Inserisci 0 per terminare l'inserimento.")

while True:
    menu()
    try:
        peso_capo = float(input("Inserisci il peso in kg del capo: "))
        if peso_capo == 0:
            break
        elif peso_capo < 0:
            print("riprova")
        elif peso_totale_kg + peso_capo > PESO_MASSIMO_KG:
            print("riprova")
        else:
            peso_totale_kg += peso_capo
    except:
        print("riprova")

