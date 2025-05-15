def modifica(clienti, codice_cliente, nuovi_kg, nuovi_euro):
    for cliente in clienti:
        if cliente['codice'] == str(codice_cliente):
            cliente['kg'] = nuovi_kg
            cliente['pagato'] = nuovi_euro * 100 
            print(f"Dati aggiornati per il cliente {codice_cliente}: {nuovi_kg} kg, {nuovi_euro} euro.")
            return
    print("Cliente non trovato.")

modifica(clienti, '199187', 5, 7)  
modifica(clienti, '123', 10, 12)  
print(clienti) 