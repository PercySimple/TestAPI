import numpy as np

matrix_size = input("Enter matrix size: ")
seed_val = input("Enter seed value: ")

np.random.seed(int(seed_val))

array1 = np.random.randint(int(seed_val), size = (int(matrix_size), int(matrix_size)))
print(array1)

arrayT = array1.transpose()
print(arrayT)

arrayDP = array1.dot(arrayT)
print(arrayDP)

trace_val = np.trace(arrayDP)
print(trace_val)