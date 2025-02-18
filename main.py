import numpy as np
arrayA = np.array([[1,0,1], [1,2,3], [1,2,4]])
arrayB = np.array([[3,1,4], [1,2,1], [3,1,1]])

#A. Código:

det = np.linalg.det(arrayA)
print(det)

# Respota: 2.0
# ---
#B. Código:

inv = np.linalg.inv(arrayB)
print(inv)

#Resposta:
#[[-0.06666667 -0.2         0.46666667]
# [-0.13333333  0.6        -0.06666667]
# [ 0.33333333 -0.         -0.33333333]]
# ---
# C. Código:

a_transposta = arrayA.T
print(a_transposta)

#Respota:
# [[1 1 1]
# [0 2 2]
# [1 3 4]]
# ---
#D. Código:

D = np.dot(arrayA,arrayB)
print(D)

# Resposta:
# [[ 6  2  5]
# [14  8  9]
# [17  9 10]]
# ---
# E. Código:

C = np.dot(-4,arrayB)
D = arrayA + C

print(D)


# Resposta:
# [[-11  -4 -15]
# [ -3  -6  -1]
# [-11  -2   0]]