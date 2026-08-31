navn="Maksym"
alder=26
bosted="Oslo"

print(navn)
print(alder)
print(bosted)

pris=17.5
antall=7
total=pris*antall
print(total)

a=27.35
b=33.79

sum=a+b

navn=input("Hei, hva heter du? ")
alder=int(input("Hvor gammal er du? "))
print("Om fem år er du ", (alder+5))
print("Om ti år er du ", (alder+10))
print("Om tjue år er du ", (alder+20))
step=int(input("Tast inn antall år fra nå: "))
print("Da blir du: ",(alder+step)," år gammel")

#kalkulator

prisPerStykk=float(input("Gi pris per stykk: "))
antall=int(input("Gi antall: "))
rabatt=int(input("Rabatt? I prosent "))

sumFørRabatt=(prisPerStykk*1*antall)
sumEtterRabatt=(prisPerStykk*(1-(rabatt/100))*antall)

print("Pris før rabatt   ", sumFørRabatt)
print("Pris etter rabatt ", sumEtterRabatt)
