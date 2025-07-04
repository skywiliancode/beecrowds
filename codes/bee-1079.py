N = int(input())
resultado = []

for i in range(N):
    numeros = list(map(float, input().split(' ')))
    resultado.append((numeros[0] * 2 + numeros[1] * 3 + numeros[2] * 5)/10)

for num in resultado:
    print(f"{num:.1f}")
