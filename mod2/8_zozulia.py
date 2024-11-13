import sys

k = int(sys.argv[1])
print(f"Ви ввели число: {k}")

arr = [3, 2, -7, -9, 1, 0, -2, 1, -2, 1, 2, -6, -7, -9, 0, 6, 1, 8, 4, 4, -1, 1]

if k <= 0:
    print("Число k повинно бути більше 0")
else:
    negatives_less_k = [x for x in arr if x < 0 and x < k]
    positives_less_k = [x for x in arr if x >= 0 and x < k]
    k_with_star = [f"{k}*"]
    greater_than_k = [x for x in arr if x > k]

    result = negatives_less_k + positives_less_k + k_with_star + greater_than_k

    print("Модифікований масив:")
    print(" ".join(map(str, result)))
