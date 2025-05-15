def converti_in_dollari(euro):
    return euro * (1 / 0.89)

def converti_clienti_in_dollari(clienti):
    clienti_in_dollari = []
    for cliente in clienti:
        cliente_converted = cliente.copy()
        cliente_converted['euro'] = converti_in_dollari(cliente['pagato'] / 100)
        clienti_in_dollari.append(cliente_converted)
    return clienti_in_dollari

clienti_in_dollari = converti_clienti_in_dollari(clienti)
print("Dati dei clienti con prezzi in dollari:")
for cliente in clienti_in_dollari:
    print(f"Codice: {cliente['codice']}, kg: {cliente['kg']}, euro: {cliente['euro']} USD")
