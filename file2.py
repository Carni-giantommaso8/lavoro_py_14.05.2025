def menu ():
    print("0 per fermare il programma : ")
    print("1 per inserire il codice giusto per aprire la porta : ")

def apertura (tentativi_rimasti):
    x = input("inserisci il codice per aprire la porta: ")
    codice = "123456"  

    if len(x) != 6 :
        print("Il codice deve essere di 6 cifre.")
        return tentativi_rimasti - 1
    elif x == codice:
        print("Codice corretto!")
        return -1 
    else:
        print("Codice sbagliato bip bip bip allarme allarme allarme!")
        return tentativi_rimasti - 1

tentativi = 3
while True:
    menu()
    scelta = int(input(f"Scegli cosa fare hai {tentativi} tentativi rimasti : "))
    if scelta == 0:
        break
    elif scelta == 1:
        if tentativi > 0:
            tentativi = apertura(tentativi)
            if tentativi == -1:
                break 
        else:
            print("Hai esaurito i tentativi. Riprova più tardi.")
    else:
        print("Scelta non valida. Riprova.")
