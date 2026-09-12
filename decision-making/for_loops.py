import random
salary = [90, 50, 78, 34, 78, 88, 909, 36, 78, 908, 234, 22, 55, 78, 89, 79, 45, 54, 78, 234, 76, 89]

n = len(salary)

i = 10

while i >= 0: 
    idx = random.randint(0, n - 1)
    
    print(salary[idx])

    i -= 1