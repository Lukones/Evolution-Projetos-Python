matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(F'Digite um valor para [{l}, {c}]: '))
print('-*' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(F'[{matriz[l][c]:^5}]', end='')
    print()