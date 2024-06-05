def fizz_buzz_sum(target):
#  problem link: https://datalemur.com/questions/python-fizz-buzz-sum
  a, b = 3, 5
  ans =0
  iter = 1 
  c, d = 3, 5
  while(c < target or  d < target):
    c = a * iter
    d  = b * iter

    if c < 10: 
      ans += c
    if d < 10: 
      ans += d
    iter += 1

  return ans

# expected : 23
print(fizz_buzz_sum(10))