import numpy as np
def eigen(A):
    m = np.matrix(A)
    val, vect = np.linalg.eig(A)
    return val, vect

n = int(input("Enter size of square matrix"))
print("Enter each row of numbers separated by commas")

m = []
for i in range(n):
    temp = input(str(i+1)+"th row :").split(',')
    m.append([int(x) for x in temp])

val, vect = eigen(m)

print("\nThe eigenvalues  are :\n")
for i in val:
    print(i)
print("\nThe eigenvectors  are :\n")
for i in range(len(val)):
	print(vect[i])