PESO_MASSIMO_KG = 9

peso_totale_kg = 0

print("Inserisci il peso in kg di ogni capo di vestiario.")
print("Il peso massimo consentito è {PESO_MASSIMO_KG} kg.")
print("Inserisci 0 per terminare l'inserimento.")

while True:
    try:
        peso_capo = float(input("Inserisci il peso in kg del capo: "))
        if peso_capo == 0:
            break
        elif peso_capo < 0:
            print("Errore: il peso non può essere negativo.")
        elif peso_totale_kg + peso_capo > PESO_MASSIMO_KG:
            print("Errore: il peso inserito farebbe superare il limite di {PESO_MASSIMO_KG} kg.")
        else:
            peso_totale_kg += peso_capo
    except:
        print("Errore")

