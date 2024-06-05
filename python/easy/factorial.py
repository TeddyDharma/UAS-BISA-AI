def factorial(n):
#  function for factorial
  if n == 0: 
    return 1
  else:
    return n * factorial(n - 1)
    


# print the result 
print(factorial(5))
# result : 120
# expected : 120