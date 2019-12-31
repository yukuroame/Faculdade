import random

arquivo = open('Gera 100 numeros.txt', 'w')
for x in range(100):
    x = random.randint(1, 100)
    print(x)
    arquivo.write('%d\n' % x)
arquivo.close()

arquivo = open('Gera 1000 numeros.txt', 'w')
for x in range(1000):
    x = random.randint(1, 1000)
    print(x)
    arquivo.write('%d\n' % x)
arquivo.close()

arquivo = open('Gera 5000 numeros.txt', 'w')
for x in range(5000):
    x = random.randint(1, 5000)
    print(x)
    arquivo.write('%d\n' % x)
arquivo.close()