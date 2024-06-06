def max_subarray_sum(input):
    # problem link  : https://datalemur.com/questions/python-largest-contiguous-subarray-sum
    max =0
    start_index = 0
    sum = 0
    for len_ in range(2, len(input)):
        while(start_index + len_ <= len(input)): 
            array = input[start_index : start_index + len_]
            for element in array: 
                sum += element
           
            if sum > max: 
                max = sum 
            start_index +=1 
            sum = 0
        start_index = 0 
       

    return max

#  expected : 11, beacause 9 + 2
print(max_subarray_sum([-1, -3, 5, -4, 3, -6, 9, 2]))