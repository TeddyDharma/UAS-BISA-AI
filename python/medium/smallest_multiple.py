def smallest_multiple(target : list):
  
#  problem link : https://datalemur.com/questions/python-smallest-multiple
  smallest_multiple_result = 1
#  cara kerja sama seperti mencari kpk, jadi nilai[i] dimoduluskan dengan nilai[i + idx] dengan idx = 1..n dan  nilai[i + idx] mode nilai[i]  = 0 dan  nilai[i + idx] >  nilai[i[ maaka ubah  nilai[i] menjadi 1 begitupun sebaliknya
  for i in range(len(target) - 1): 
    for j in range(i +1, len(target)): 
      if target[j] % target[i] == 0 and target[i] != 1 and target[j] > target[i]:
        target[i] = 1 
      elif target[i]  % target[j] == 0 and target[j] != 1 and target[i] > target[j]: 
        target[j] == 1
# kalikan semua elemen yang ada di dalam list untuk mendapatkan hasil
  for number in target:
    smallest_multiple_result *= number
  return smallest_multiple_result

# expected : 60
print(smallest_multiple([1, 2, 3, 4, 5]))