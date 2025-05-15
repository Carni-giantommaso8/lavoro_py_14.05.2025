def clienti_con_piu_di_5_kg(clienti):
    return [cliente['codice'] for cliente in clienti if cliente['kg'] > 5]

codici_clienti_5_kg = clienti_con_piu_di_5_kg(clienti)
print(f"Codici clienti che hanno lavato più di 5 kg: {codici_clienti_5_kg}")
