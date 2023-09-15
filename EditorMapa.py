import random

mapa = open("map.txt", 'w')
map = {'x':10, 'y':10}

mapa.write("Mapa x=10, y=10\n")

random.seed()

for i in range(map['x']):
    for i in range(map['y']):
        if(random.getrandbits(2)>2):
            mapa.write('*')
        else:
            mapa.write('#')
    mapa.write("\n")

mapa.close()