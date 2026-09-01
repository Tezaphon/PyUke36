#oppgave 1

#x=float(input("Gi et tall: "))
#if x<0:
#    print("Tallet er negativt")
#elif x==0:
#    print("Tallet er null")
#elif x>0:
#    print("Tallet er positivt")

#oppgave 2

alder=int(input("Gi alder: "))
student=int(input("Er du student?  Tast 1 for 'Ja' "))

if alder<6:
    print("Barn tenger ikke bilett")
elif alder>6 and alder<17:
    print("Ungdomsbilett - 50 NOK")
elif alder>66:
    print("Seniorbilett - 50 NOK")
elif student==1 and alder<30:
    print("Studentbilett - 60 NOK")
elif alder>18 and alder<66:
    print("Voksenbilett - 100 NOK")