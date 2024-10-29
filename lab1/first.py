def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

start = min(a, b)
end = max(a, b)

print(f"Прості числа між {start} та {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)
