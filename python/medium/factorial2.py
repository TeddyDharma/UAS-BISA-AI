# problem link : https://datalemur.com/questions/python-factorial-trailing-zeroes


def trailing_zeroes(n):
  
  factorial = 1

# search for factorial value
  for i in range(n): 
    factorial = factorial * n 
    n -= 1 

# convert to string
  factorial = str(factorial)
  
#  counting zero char
  count_zero = 0
  for char_i in factorial: 
    if char_i == "0": 
      count_zero += 1

  return count_zero
   


#  5! = 120 and 120 has exactly 1 trailing zero or 10! = 3628800 return 2, becuase there are two trailing zeroes.
print(trailing_zeroes(10))