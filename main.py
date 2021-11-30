##Enkel kalkulator skrevet i python

#Først oppretter jeg en variabel. Variabler bruker man til å large verdier og data i.
#operation i dette tilfellet er en string. En string er tekst i programmering.
#Andre typer variabler  er:
#int som er heltall(10, 56,434423, 3)
#float som er desimaltall (1.0, 3.14, 11,7)
operation = input("Hvilken operasjon ønsker du?\n1 - pluss\n2 - minus\n3 - gange\n4 - dele\nSkrin inn her: ")
#Her spør jeg om en string som skal lagres i operation. \n er en indikator på at det som kommer etter
#skal printes på en ny linje

#Samme prosess her. Spør bruker om å taste inn tall, lagrer det i en string som heter "first_number".
#Man kan ikke bruke mellomrom når man oppretter variabler. Standard prosedyre er understrek.
first_number = input("Hva er første tall?\nSkriv inn her: ")
second_number = input("Hva er andre tall?\nSkriv inn her: ")

#Etter jeg har tallene mine, må jeg gjøre en string(tekst) til en int(heltall) for å kunne utføre matematiske operasjoner på de.
int_first_number = int(first_number)
int_second_number = int(second_number)
#Oppretter en ny variabel som heter "int_first_number" som gjør teksten i "first_number" til tall,
# slik at python skjønner hva den skal gjøre.
#Hvis du skriver inn tekst i kalkulatoren, kommer det bare til å bli krøll.

#En liten sjekk her for om man har skrevet riktig tall. Dette trenger ikke du tenke så mye på, det er litt over
#det du skal kunne.
choice = input("Du har skrevet inn " + first_number + " og " + second_number + " Stemmer dette? (y/n) ")

#Samme her. Bare noe jeg la inn for gøy, men man kan se at man går gjennom samme prosess som ovenfor for å velge tall.
while choice == 'n':
    first_number = input("Hva er første tall?\nSkriv inn her: ")
    second_number = input("Hva er andre tall?\nSkriv inn her: ")
    int_first_number = int(first_number)
    int_second_number = int(second_number)
    choice = input("Du har skrevet inn " + first_number + " og " + second_number + " Stemmer dette? (y/n)  ")


#Her er en funksjon. En funksjon starter alltid med 'def'. Det som står mellom parantesen, er det man kan putte inn i funksjonen.
#Denne funksjonen heter f(Man kan velge helt selv) og skal få ett parameter (x).
#I denne funksjonen, sjekker den hvilken matamatisk operasjon du valgte helt i starten (1 for pluss, 2 for minus osv)
#Da går den gjennom funksjonen, helt til et av tallene stemmer der det står 'case'.
#Funksjonen vil da kjøre koden som står under den casen. For eksempel i case 1, plusser den de to tallene du skrev inn.
#Her har vi kun definert funksjonen, men den blir ikke brukt bare fordi den er definert.
def f(x):
    match x:
        case '1':
            result =  int_first_number+int_second_number
            print("Resultatet er. " + str(result))
        case '2':
            result = int_first_number - int_second_number
            print("Resultatet er. " + str(result))
        case '3':
            result = int_first_number * int_second_number
            print("Resultatet er. " + str(result))
        case '4':
            result = int_first_number / int_second_number
            print("Resultatet er. " + str(result))

#Her kaller vi på funksjonen, og sier at den skal ta inn stringen(teksten) du skrev inn da du valgte operasjon
#Husk at selv om du skrev 2 for minus, så går det som tekst og ikke tall, siden input alltid skriver alt som tekst.
f(operation)