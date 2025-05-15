persone = []

def inserisci_dati():
    while True:
        codice_cliente = int(input("Inserisci il codice del cliente e scrivi 999999 per terminare: "))

        if codice_cliente == 999999:
            break
        
        kg_lavati = float(input(f"Inserisci i kg lavati dal cliente {codice_cliente}: "))
        pagamento = float(input(f"Inserisci gli euro pagati dal cliente {codice_cliente}: "))
        
        persone.append({
            "codice": codice_cliente,
            "kg": kg_lavati,
            "euro": pagamento
        })
    
    totale_kg = sum(cliente["kg"] for cliente in persone)
    totale_pagato = sum(cliente["euro"] for cliente in persone)
    media_kg = totale_kg / len(persone) if len(persone) > 0 else 0
    
    massimo_pagato = persone[0]
    for cliente in persone:
        if cliente["euro"] > massimo_pagato["euro"]:
            massimo_pagato = cliente
    
    print(f"Totale kg lavati: {totale_kg}")
    print(f"Media kg lavati per cliente: {media_kg}")
    print(f"Totale pagato dai persone: {totale_pagato}")
    print(f"Cliente che ha pagato di più: Codice {massimo_pagato['codice']} con {massimo_pagato['euro']} euro")

inserisci_dati()
