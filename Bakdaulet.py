import random

# 1-ші тапсырма
a = [random.randint(1, 100) for _ in range(10)]
print("Массив a:", a)

# 5-ке қалдықсыз бөлінетін сандарды таңдау
div5 = [x for x in a if x % 5 == 0]

if div5:
    min_div5 = min(div5)
    print("5-ке бөлінетін ең кіші сан:", min_div5)
else:
    print("Массивте 5-ке бөлінетін сан жоқ")

# 2-ші тапсырма
A = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
print("\nМатрица A:")
for row in A:
    print(row)

# Қосымша диагональ (i+j = n-1)
n = 4
additional_diag = [A[i][n - 1 - i] for i in range(n)]
print("Қосымша диагональ элементтері:", additional_diag)

min_additional = min(additional_diag)
print("Қосымша диагональдағы ең кіші элемент:", min_additional)