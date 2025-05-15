def menu ():
    print("0 per fermare il programma ")
    print("1 per inserire il codice giusto per aprire la porta")

def apertura ():
    x = input("inserisci il codice per aprire la porta: ")
    codice = ("123456")

    if len(x) != 6 :
        print("il codice deve essere di 6 cifre")
        print("")
    else:
        if x == codice:
            print("hai inserito il codice giusto")
            print("")
            
        if x != codice:
            print("hai sbagliato il codice bip bip bip allarme allarme allarme")
            print("")

while True:
    menu()
    scelta = int(input("scegli cosa fare: "))
    print("")

    if scelta == 0:
        break
    if scelta == 1:
        apertura()

