liste=[]
print("Hallo, dette er et program for å lage lister")

def optionCall():
    print("-----------------------------------------")
    print("Tast:")
    print("1 for å vise oppgaver i listen")
    print("2 for å legge en oppgave til listen")
    print("3 for å fjerne en oppgave fra listen")
    print("9 for å dra tilbake til denne menyen")
    print("0 for å stoppe programmet")
    return int(input("Tast en option: "))

liv=True
while liv==True:
    chosenOption=optionCall()
    print(chosenOption)


    if chosenOption==0:
        liv=False
    elif chosenOption==1:
        for i in liste:
            print(i)
    elif chosenOption==2:
        nyOppgave=input("Skriv inn ny oppgave: ")
        liste.append(nyOppgave)
    elif chosenOption==3:
        index=int(input("Tast inn oppgavens nummer for å fjerne den: "))
        list.pop(index-1)
    elif chosenOption==9
