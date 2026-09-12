# numbers = [12, 23, 43, 23, 45]

import random 

random.seed(0)
numbers = [
    random.randint(0, 1000) for i in range(20)
]
# print(numbers)

idx = (len(numbers) // 2)
# print(numbers[1:4], numbers[5:10])
print(numbers[::-1])