from colorama import Fore, Back, Style

ledger=["Tomt","og","stille"]
print("Hallo, dette er et program for å lage lister")

def optionCall():
    print("=========================================")
    print("Tast:")
    print("1 for å vise oppgaver i listen")
    print("2 for å legge en oppgave til listen")
    print("3 for å fjerne en oppgave fra listen")
    print("0 for å stoppe programmet")
    print("-----------------------------------------")
    x=int(input("Tast en option: "))
    print("-----------------------------------------")
    return x
def showList():
    print("-----------------------------------------")
        for i in ledger:
            print(Fore.BLUE+i+Fore.RESET)

liv=True
while liv==True:
    chosenOption=optionCall()
    #print(chosenOption)


    if chosenOption==0:
        liv=False
    elif chosenOption==1:
        showList()
    elif chosenOption==2:
        nyOppgave=input(Fore.GREEN+"Skriv inn ny oppgave: "+Fore.RESET)
        ledger.append(nyOppgave)
        showList()

    elif chosenOption==3:
        index=(int(input(Fore.RED+"Tast inn oppgavens nummer for å fjerne den: "+Fore.RESET))-1)
        ledger.pop(index)
        print("-----------------------------------------")
        showList()

