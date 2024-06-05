# problem link : https://datalemur.com/questions/python-two-sum

def two_sum(input: list[int], target: int) -> list[int]:
    answear = []
    for i in range(len(input)-1): 
        for j in range(i + 1, len(input)): 
            if input[j] + input[i] ==  target: 
                answear.append([i, j])
    return answear[0]

# input = [1, 4, 6, 10], target = 11 Output: [0, 3]
print(two_sum( [1, 4, 6, 10], 11))