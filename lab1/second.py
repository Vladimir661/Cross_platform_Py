def fib(k):
    if k <= 0:
        return []
    elif k == 1:
        return [0]
    elif k == 2:
        return [0, 1]
    else:
        fib_list = fib(k - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list

k = int(input("Введіть число k: "))
fib_numbers = fib(k)

print(f"Перші {k} чисел Фібоначчі: {fib_numbers}")
