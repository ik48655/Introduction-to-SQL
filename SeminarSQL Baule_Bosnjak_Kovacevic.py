import os
from itertools import combinations

lista5 = [['DI','B'],['AJ','F'],['GB','FJE'],['AJ','HD'],['I','CG']]
R5 = "ABCDEFGHIJ"
lista4 = [['AD','B'],['D','E'],['B','C']]
R4 = "ABCDE"
lista3 = [['A','B'],['A','D'],['A','H'],['C','B'],['B','E'],['I','J'],['H','G'],['D','F']]
R3 = "ABCDEFGHIJ"
lista2 = [['DI', 'B'], ['AJ', 'F'], ['GB', 'FJE'], ['AJ', 'HD'], ['I', 'CG']]
R2 = "ABCDEFGHIJ"
lista1 = [['A', 'BCDE'], ['C', 'F']]
R1 = "ABCDEF"

baza = [[lista1, R1],[lista2, R2],[lista3, R3],[lista4, R4],[lista5, R5]]

def sortiraj_str(str1): 
  after_sort = ''.join(sorted(str1))
  return after_sort


def nadskup(nad, pod):
    for i in pod:  
        if i not in nad:
            return 0
    return 1


def algoritam(lista, R): 
    st = []
    kandidati = []

    for i in range(1, len(R)):
        temp = combinations(R, i)
        st += temp
    for tup in st:
        tup = ''.join(tup)
        if(kandidati and len(kandidati[0]) < len(tup)):
            break 
        tup_st = "" 
        for rel in lista:
            if nadskup(tup, rel[0]): 
                tup_st += rel[1]
            tup_st = sortiraj_str(tup_st)
        if tup_st == "":
            continue
        tup_st2 = tup_st + tup 
        tup_st2 = "".join(set(tup_st2)) 
        br = 0
        while br < 100: 
            for rel in lista:
                if nadskup(tup_st2,rel[0]): 
                    tup_st2 += rel[1] 
                    tup_st2 = "".join(set(tup_st2))
            br+=1
        if nadskup(R,tup_st2) and len(R) == len(tup_st2):
            kandidati.append(tup) 
    print("\n", kandidati)
    print(" ")
    return kandidati
            

def izbrisi(velkaLista):
    broj = 0
    for i in velkaLista:
        print("Lista ", broj, " ", i)
        broj += 1
    os.system('CLS')
    x = int(input("Koju funkcionalnu ovisnost želite izbrisati? "))
    velkaLista.pop(x)
    os.system('CLS')

        
def unosListe():
    glavnaLista = []
    os.system('CLS')
    x = int(input("Broj funkcionalnih ovisnosti: "))
    for i in range(x):
        y = input("Ključ atributa: ")
        z = input("Vrijednost atributa: ")
        y = y.upper()
        z = z.upper()
        malaLista = [y, z]
        glavnaLista.append(malaLista)
    print(glavnaLista)
    R = input("R: ")
    R = R.upper()
    nepostojeci = False
    for i in glavnaLista:
        for j in i:
            if j[0] not in R and j[1] not in R:
                nepostojeci = True
    if nepostojeci == False:
        baza.append([glavnaLista, R])
    os.system('CLS')


def izbornik():
    print("Za unos nove liste pritisnuti U.\n")
    print("Za brisanje liste pritisnuti B.\n")
    print("Za ispis primarnih ključeva pritisnuti P.\n")
    print("Za dekompoziciju do 3. normalne forme pritisnusti D.\n")
    print("Za izlaz iz terminala pritisnuti X.\n")
    slovo = input("")
    if (slovo == "U" or slovo == "u"):
        print()
        unosListe()
    elif (slovo == "B" or slovo == "b"):
        os.system('CLS')
        ind = 0
        for i in baza:
            print("[", ind, "] -", i[0],"(", i[1], ")")
            ind += 1
        print("\nUnesite indeks liste kojoj želite izbrisati funkcionalne ovisnosti: ")
        ind = int(input(""))
        if ind < len(baza):
            izbrisi(baza[ind][0])
    elif (slovo == "D" or slovo == "d"):
        os.system('CLS')
        ind = 0
        for i in baza:
            print("[", ind, "] -", i[0], "(", i[1], ")")
            ind += 1
        print("\nUnesite broj primjera za koji želite napraviti dekompoziciju: ")
        ind = int(input(""))
        if ind < len(baza):
            kljucevi = algoritam(baza[ind][0], baza[ind][1])
            dekompozicija(kljucevi,baza[ind][0])
    elif (slovo == "P" or slovo == "p"):
        os.system('CLS')
        ind = 0
        for i in baza:
            print("[", ind, "] -", i[0], "(", i[1], ")")
            ind += 1
        print("\nUnesite broj primjera kojem želite ispisati primarne ključeve: ")
        ind = int(input(""))
        if ind < len(baza):
            algoritam(baza[ind][0], baza[ind][1])
    elif (slovo == "X" or slovo == "x"):
         exit()

def razdvoji(fo):
    left = []
    right = []
    for i in fo:
        left.append(i[0])
        right.append(i[1])
    return left,right

def usporedistring(string1,string2):
    if (string1 == string2):
        return 1
    return 0

def provjeriniz(arr,string):
    if arr == []:
        arr.append(string)
        return arr
    for i in arr:
        if usporedistring(i,string):
            return arr
    arr.append(string)
    return arr

def dekompozicija(keys,fo):
    left, right = razdvoji(fo)
    arr = []
    for i in keys:
        for j in range(0,len(left)):
            arr = provjeriniz(arr,left[j]+right[j])
        arr = provjeriniz(arr, i)
        print(i+': ',arr)
        print(" ")
        arr = []
 
while True:
    izbornik()


#print(lista1)
#lijevi,desni = razdvoji(lista1)
#print(lijevi)
#print(desni)