'''
1.1 Feladat
Készíts egy programot, amely a felhasználótól keresztneveket kér be egészen addig, amíg az ENTER-t nem üt (nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!
-----------------------
1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki.
'''


'''
lista = []
while True:
    beker = input('Keresztnév: ')
    if beker == "":
        break
    lista.append(beker)
print(lista)
'''

lista = []
x = 0
while x <3:
    beker = input('Keresztnév: ')
    if beker != "":
        x += 1
    if x == 3:
        print('Nincs több lehetőséged név megadására!')
    if beker == "":
        break
    lista.append(beker)
print(lista)
