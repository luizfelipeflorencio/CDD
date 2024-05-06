A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]

for x in range(10):
    A[x] = int(input("Digite um numero: "))

X = int(input("digite o multiplicador: "))

for y in range(10):
    M[y] = A[y] * X
print(A)
print(X)
print(M)