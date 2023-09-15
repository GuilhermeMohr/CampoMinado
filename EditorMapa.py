import random

mapa = open("map.txt", 'w')
map = {'x':10, 'y':10, "vazio":0}

random.seed()

for i in range(map['x']):
    for i in range(map['y']):
        if(random.getrandbits(3)>6):
            mapa.write('*,')
        else:
            map["vazio"] += 1
            mapa.write('#,')
    mapa.write("\n")
    
mapa.write(f"Mapa x={map['x']}\ny={map['y']}\nVazio={map['vazio']}")

mapa.close()