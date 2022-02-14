'''

1.4 Feladat
Készíts egy programot, amely sztringeket tartalmazó listaelemek leképezését valósítja meg. A leképezéshez a sztringek metódusait ezen az oldalon bemutató listából válassz egyet! A program írja ki az eredeti és a generált listát is a képernyőre!
'''

lista1=['egy','ketto','harom','negy']

lista2=[szo.rjust(6,'f') for szo in lista1]
print(lista2)