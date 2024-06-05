def has_merge_conflict(pull_requests)-> bool:
  is_merged_conflict = False

#   first iteration
  for idx in range(1, len(pull_requests)): 
    temp = pull_requests[idx]
    temp_2 = pull_requests[idx - 1]
    # checking merge
    for index, _ in enumerate(temp): 
      if temp[index]  >  temp_2[index]: 
        is_merged_conflict = True
        break



  return is_merged_conflict


print(f'result : {has_merge_conflict([[5, 10], [15, 40], [25, 50]])}')
print(f'EXPECTED : {True}')
print(f'result : {has_merge_conflict([[30, 40], [10, 20], [5, 8]])}')
print(f'EXPECTED : {False}')