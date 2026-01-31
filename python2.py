#--------------------------
'''
    A kereses_a_listablan nevű függvény.
    Első bemeneti paraméter egy lista,
    második bemeneti paraméter egy szám.
    A visszatérési érték a paraméterként megadott szám
        első előfordulási helye a listában.
    
    A visszatérési érték None, ha a szám nics benne a listában.
'''
def kereses_a_listaban(lista, szam):
    pozic = 0       # Ez számolja, hogy hányadik elemnél járunk
    for i in lista:     # A lista elemeit egyesével megnézzük
        if i == szam:       # Megnézükk, hogy egyezik e a keresett számmal
            return pozic        # Ha igen, akkor visszadjuk az elem helyét
        pozic += 1      # Ha nem egyezik akkor lépünk, a következő elemre
    return None     # Ha a szám nincs a listában


#--------------------------
''' 
    A legkisebb nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legkisebb számával.
    Üres lista esetén None a visszatérési érték.
    
    A feladat megoldása során nem használhatod a min() függvényt!
'''



#--------------------------
'''
    A benne_van_a_stringben nevű függvény.
    első paraméterként egy stringet kap,
    második paraméterként egy betüt.
    Visszatérési értéke True, ha  a betü benne van a stringben.
    A visszatérési érték False, ha  a betü nics benne a stringben.
'''
def benne_van_a_stringben(string, betu):
    for i in string:        # A lista elemeit sorban megnézzük
        if i == betu:       # Ha az i megegyezik a keresett számmal
            return True     # Igaz, mert a szám benne van a listában
    return False        # Hamis, mert  a szám nincs benne a listában


#--------------------------
''' 
    A pozitivok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista pozitív számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def pozitivok_szama(pozitivok):
    poz = 0     # Ez számolja hogy hány pozitív szám van
    for i in pozitivok:     # Végig megyünk a lista minden elemén
        if i > 0:       # Megnézzük hogy a szám pozitív-e
            poz += 1        # Ha igen, akkor növeljük a számlálót
    return poz      # Vissza adjuk a pozitív számok számát


#--------------------------
''' 
    A legnagyobb  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista legnagyobb számával.
    Üres lista esetén None a visszatérési érték.

    A feladat megoldása során nem használhatod a max függvényt!
'''



#--------------------------
'''
    A paratlanok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páratlan számait tartalmazza.
'''
def paratlanok_kivalogatasa(lista):
    par = []
    for i in lista:
        if i % 2 != 0:
            par.append(i)
    return par

#--------------------------
''' 
    Az elso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér a string első karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def elso_karakter(string):
    if string == "":
        return None
    return string[0]


#--------------------------
''' 
    A negativok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista negativ számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def negativok_szama(negativok):
    neg = 0
    for i in negativok:
        if i < 0:
            neg += 1
    return neg


#--------------------------
''' 
    A parosok_szama  nevű függvény,
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def parosok_szama(parosok):
    par = 0
    for i in parosok:
        if i % 2 == 0:
            par += 1
    return par

#--------------------------
''' 
    Az osszeg  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak összegével.
    Üres lista esetén 0 a visszatérési érték.
    A feladat megoldása során nem használhatod a sum() függvényt!
'''
def osszeg(osszeg):
    ossz = 0
    for i in osszeg:
        ossz += i
    return ossz

#--------------------------
''' 
    Az utolso_karakter nevű függvény,
    paraméterként egy stringet kap és
    visszatér az adott string utolso karakterével.
    
    Üres string esetén None a visszatérési érték.
'''
def utolso_karakter(string):
    if string == "":
        return None
    return string[-1]
#--------------------------
''' 
    A lista_atlag nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak átlagával.
'''



#--------------------------
'''
    A parosok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        páros számait tartalmazza.
'''
def parosok_kivalogatasa(lista):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par


#--------------------------
''' 
    A pozitivok_kivalogatasa nevű függvény,
    visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista
        pozitiv számait tartalmazza. 
'''
def pozitivok_kivalogatasa(pozitiv):
    poz = []
    for i in pozitiv:
        if i > 0:
            poz.append(i)
    return poz


#--------------------------
'''
    A kereses_a_stringben nevű függvény,
    első paraméterként egy sztringet kap,
    második paraméterként egy betüt.
    Visszatérési érték a paraméterként megadott betü
        első előfordulási helye a stringben. 
    
    A visszatérési érték None, ha a betü nics benne a stringben.
'''
def kereses_a_stringben(string, betü):
    str = 0
    for i in string:
        if i == betü:
            return str
        str += 1
    return None


#--------------------------
''' 
    A paratlanok_szama nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér egy számokat tartalmazó lista páros számainak számával.
    
    Üres lista esetén 0 a visszatérési érték.
'''
def paratlanok_szama(paratlanok):
    par = 0
    for i in paratlanok:
        if i % 2 != 0:
            par += 1
    return par


#--------------------------
'''
    A benne_van_a_listaban nevű függvény,
    első paraméterként egy listát kap,
    második paraméterként egy számot.
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    
    Üres lista esetén a visszatérési érték False.
'''
def benne_van_a_listaban(lista, keresett):
    for i in lista:
        if i == keresett:
            return True
    return False


#--------------------------
''' 
    A szorzat  nevű függvény,
    paraméterként egy számokat tartalmazó listát kap és
    visszatér a lista számainak szorzatával.
    
    Üres lista esetén 1 a visszatérési érték.
'''
def szorzat(szorzat):
    szor = 1
    for i in szorzat:
        szor *= i
    return szor


#--------------------------
'''
    A faktorialis nevű függvény,
    visszatér a paraméterként megkapott szám faktoriálisával.
'''



#--------------------------
'''
    A negativok_kivalogatasa nevű függvény,
    visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista
      negatív számait tartalmazza.
'''
def negativok_kivalogatasa(negativok):
    neg = []
    for i in negativok:
        if i < 0:
            neg.append(i)
    return neg


#======================================================================================================================C:\beni\Informatika\10.k\Programozás\python2-main\python2-main