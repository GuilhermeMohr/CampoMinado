import EditorMapa
import os

from colorama import Fore, Back, Style

mapa = {"arquivo":open("map.txt", 'r'), 'x':0, 'y':0, "coordenadas":[], "display":[], "vazio":0}

def inicializar():
    i = mapa["arquivo"].readlines()

    ii = i[-3].split('=')
    mapa["x"] = int(ii[1])
    del i[-3]
 
    ii = i[-2].split('=')
    mapa["y"] = int(ii[1])
    del i[-2]

    ii = i[-1].split('=')
    mapa["vazio"] = int(ii[1])
    del i[-1]
 
    for linha in i:
        i = linha.split(',')
        ii = []
        iii = []
        
        for ponto in i:
            if ponto != '\n':
                ii.append(ponto)
                iii.append('#')
        mapa["coordenadas"].append(ii)
        mapa["display"].append(iii)
       
    mapa["arquivo"].close()
    
def revelar(y, x):
    i = 0
    if y+1 < mapa['y']:
        if mapa["coordenadas"][y+1][x] == '*':
            i+=1
        if mapa["coordenadas"][y+1][x-1] == '*' and x-1 >= 0:
            i+=1

    if x+1 < mapa['x']:
        if mapa["coordenadas"][y][x+1] == '*':
            i+=1
        if mapa["coordenadas"][y-1][x+1] == '*' and y-1 >= 0:
            i+=1
    
    if y+1 < mapa['y'] and x+1 < mapa['x']:
        if mapa["coordenadas"][y+1][x+1] == '*':
            i+=1

    if mapa["coordenadas"][y-1][x] == '*' and y-1 >= 0:
        i+=1
    if mapa["coordenadas"][y][x-1] == '*' and x-1 >= 0:
        i+=1
    if mapa["coordenadas"][y-1][x-1] == '*' and y-1 >= 0 and x-1 >= 0:
        i+=1
    
    if i == 0:
        if mapa["display"][y][x] == '#':
            mapa["display"][y][x] = '-'
            mapa["vazio"] -= 1
        
        if y+1 < mapa['y']:
            if mapa["display"][y+1][x] == '#':
                revelar(y+1, x)
            if mapa["display"][y+1][x-1] == '#' and x-1 >= 0:
                revelar(y+1, x-1)
                
        if x+1 < mapa['x']:
            if mapa["display"][y][x+1] == '#':
                revelar(y, x+1)
            if mapa["display"][y-1][x+1] == '#' and y-1 >= 0:
                revelar(y-1, x+1)
                
        if y+1 < mapa['y'] and x+1 < mapa['x']:
            if mapa["display"][y+1][x+1] == '#':
                revelar(y+1, x+1)

        if mapa["display"][y-1][x] == '#' and y-1 >= 0:
            revelar(y-1, x)
        if mapa["display"][y][x-1] == '#' and x-1 >= 0:
            revelar(y, x-1)
        if mapa["display"][y-1][x-1] == '#' and y-1 >= 0 and x-1 >= 0:
            revelar(y-1, x-1)
        
    else:
        if mapa["display"][y][x] == '#':
            mapa["display"][y][x] = i
            mapa["vazio"] -= 1
        
 
inicializar()

win = False

while(True):
    if mapa["vazio"] == 0:
        win = True
        break;

    os.system("cls")
    i = 1
    print("  1 2 3 4 5 6 7 8 9 10")
    for coluna in mapa["display"]:
        if  i == 10:
            print(f"{i}", end='')
        else:
            print(f"{i} ", end='')
        i+=1
        for ponto in coluna:
            print(ponto, end='')
            print(" ", end='')
        print()

    x = 0
    y = 0
    while(True):
        print("x:", end='')
        x = int(input()) -1
        print("y:", end='')
        y = int(input()) -1
     
        if x < mapa['x'] and y < mapa['y'] and x >= 0 and y >= 0:
            break;
        else:
            print("Ocorreu um erro, repita o preocesso.")
        

    if mapa["coordenadas"][y][x] == '*':
        mapa["display"][y][x] = '*'
        break;
    else:
        revelar(y, x)
        
os.system("cls")
if win:
    print(Fore.GREEN + """
    _____.___.               __      __                    
    \\__  |   | ____  __ __  /  \\    /  \\____   ____     
     /   |   |/  _ \\|  |  \\ \\   \\/\\/   /  _ \\ /    \\    
     \\____   (  <_> )  |  /  \\        (  <_> )   |  \\ 
     / ______|\\____/|____/    \\__/\\  / \\____/|___|  /  
     \\/                            \\/             \\/    """)
else:
    print(Fore.RED + """
      ________                        ________                         
     / _____ / _____    _____   ____   \\_____  \\___   __ ___________ 
    /   \\  ___\\__   \\  /     \\_/ __ \\   /   |   \\  \\ / // __ \\_  __ \\     
    \\    \\_\\  \\/ __  \\|  Y Y  \\  ___/  /    |    \\    /\\  ___/|  | \\/
     \\______  (____  / __|_|  /\__  >  \______  / \\_ /  \\___  >__|    
            \\/     \\/       \\/    \\/          \\/           \\/        """)
print(Fore.RESET + "")