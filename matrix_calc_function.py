import numpy as np

def matrix_calc(x, n, operation):
  if(x.isnumeric() & n.isnumeric()):
    matrix_size = int(x)
    seed_val = int(n)
    np.random.seed(seed_val)
    array1 = np.random.randint(seed_val, size = (matrix_size, matrix_size))
    arrayT = array1.transpose()
    if operation == "Dot product":
      result = array1.dot(arrayT)
    else:
      operation == "Trace value"
      result = np.trace(array1.dot(arrayT))
  else:
    result = "Please enter a valid number in the input fields"
  return result
