import time


materiale = {'pal': 25, 'mdf': 35}
culori = {'rosu': 10, 'galben': 3.5, 'venghe': 1.2, 'alb': 1.5, 'maro': 1.7, 'portocaliu': 1.9, 'pictat': 4.5}
dim = {'lungime': 2800, 'lățime': 2070}
meniu_s = ('Alegeți materialul', 'Alegeți culoarea', 'Introduceți lungimea cm', 'Introduceți lățime cm')
articole = []


def se_cauta(lista, materiale, culori):
    """caută prețul materialului și a culorii"""
    total = 0
    for i in range(len(lista)):
        if i == 0:
            pret_material = round(list(materiale.items())[i][1] * lista[-1], 2)
            print(f'- material {list(materiale.items())[i][0]} cu prețul {list(materiale.items())[i][1]}/mp2')
            print(f'Cost material ales: {pret_material}')
        elif i == 1:
            pret_culoare = round(list(culori.items())[i][1] * lista[-1], 2)
            print(f'- culoare {list(culori.items())[i][0]} cu prețul {list(culori.items())[i][1]}/mp2')
            print(f'Cost culoare aleasă: {pret_culoare}')
    total = pret_material + pret_culoare
    print(f'Prețul materialului este: {total}')
    lista.append(total)
    return lista


def calcul_preț(lista, materiale, culori):
    """se calculează prețul materialelor"""
    preturi = []
    for i in lista:
        if len(i) < 6:
            se_cauta(i, materiale, culori)
    for i in lista:
        preturi.append(i[-1])
    total = round(sum(preturi), 2)
    print(f'Prețul total pentru materialele alese este: {total}')
    time.sleep(1)


def enumerator(lista):
    """create user inputs"""
    rez = []
    for i in lista:
        a = input(i + ': ')
        rez.append(a)
    lungime = int(rez[-2])
    latime = int(rez[-1])
    mp2 = round((lungime * latime) * 0.0001, 2)
    rez.append(mp2)
    return rez


def lista_materiale(lista):
    """Se afișează lista materialelor"""
    nr_mat = 0
    for k, v in lista.items():
        print(f'{nr_mat} - {k} având prețul de: {v}/mp2')
        nr_mat += 1


def _add_material(articole, dimensiuni):
    articole.append(dimensiuni)
    return articole


def add_material(articole, m=meniu_s):
    '''se adaugă un material în lista primind dimensiunile de la utilizator'''
    dimensiuni = enumerator(m).copy()
    return _add_material(articole, dimensiuni)


def meniu(articole):
    '''meniul calculatorului de materiale'''
    print('''
    ^Calculator materiale^

    1. Adaugă un material

    Pentru a opri programul folosiți litera e
    ''')

    a = input('Selectați opțiunea: ')
    if a == 'e':
        print('\nMulțumim pentru că ați folosit programul!')
        exit(0)
    elif a == '1':
        print('*Materialele disponibile: ')
        lista_materiale(materiale)
        print('*Culorile disponibile:')
        lista_materiale(culori)
        add_material(articole)
        calcul_preț(articole, materiale, culori)
    else:
        print('!Alegeți opțiunea corectă!')


while True:
    meniu(articole)
    # de șters
    # print(f'Materialele sunt: {articole}')
