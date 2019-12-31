a = open('Gera 100 numeros.txt', 'r')
a = a.readlines()
A = [int(v) for v in a]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print('100 números ordenados!')
arquivo = open('100 números ordenados.txt', 'w')
for i in range(len(A)):
    print('%d' % A[i])
    arquivo.write('%d\n' % A[i])
arquivo.close()

#--------------------------------------------------

a = open('Gera 1000 numeros.txt', 'r')
a = a.readlines()
A = [int(v) for v in a]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print('1000 números ordenados!')
arquivo = open('1000 números ordenados.txt', 'w')
for i in range(len(A)):
    print('%d' % A[i])
    arquivo.write('%d\n' % A[i])
arquivo.close()

#--------------------------------------------------

a = open('Gera 5000 numeros.txt', 'r')
a = a.readlines()
A = [int(v) for v in a]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print('5000 números ordenados!')
arquivo = open('5000 números ordenados.txt', 'w')
for i in range(len(A)):
    print('%d' % A[i])
    arquivo.write('%d\n' % A[i])
arquivo.close()
