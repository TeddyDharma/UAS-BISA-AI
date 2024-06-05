def largest_prime_factor(target): 
  
# problem links : https://datalemur.com/questions/python-largest-prime-factor
  max = 0
  for number in range(2, target): 
    if target % number == 0: 
       factor =0
       for i in range(1, number + 1): 
         if number % i == 0: 
            factor +=1
       if factor == 2: 
         if max < number: 
            max = number
  return max

# expected : 7
print(largest_prime_factor(42))
