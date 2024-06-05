import numpy as np
#  probleme : https://datalemur.com/questions/python-missing-integer
def missing_int(input: list[int])-> int:
  max_value = input[np.argmax(input)]
  missing_value = 0
  for i in range(max_value): 
    if i not in input: 
      missing_value = i
  return missing_value
      

# expected : 2
print(missing_int([0,1,3]))