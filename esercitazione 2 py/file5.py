giorni_cliente_1 = [3, 5, 6, 18, 19, 23, 30]
giorni_cliente_2 = [1, 2, 3, 5, 6, 10, 12, 19, 23]
giorni_cliente_3 = [1, 5, 7, 19, 23, 25, 30]

giorni_tutti_presenti = []
for giorno in giorni_cliente_1:
    if giorno in giorni_cliente_2 and giorno in giorni_cliente_3:
        giorni_tutti_presenti.append(giorno)

giorni_nessuno_presenti = []
for giorno in range(1, 31):
    if giorno not in giorni_cliente_1 and giorno not in giorni_cliente_2 and giorno not in giorni_cliente_3:
        giorni_nessuno_presenti.append(giorno)

giorni_almeno_uno_presenti = []
for giorno in range(1, 31):
    if giorno in giorni_cliente_1 or giorno in giorni_cliente_2 or giorno in giorni_cliente_3:
        giorni_almeno_uno_presenti.append(giorno)

print(f"Giorni in cui si sono presentati tutti e tre i clienti: {giorni_tutti_presenti}")
print(f"Giorni in cui non si è presentato nessuno dei tre clienti: {giorni_nessuno_presenti}")
print(f"Giorni in cui si è presentato almeno uno dei tre clienti: {giorni_almeno_uno_presenti}")
