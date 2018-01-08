def is_perfect(n):
    return sum([i for i in range(2, int(n / 2) + 1) if n % i == 0]) + 1 == n

print ("Input number:")

print(is_perfect(int(input())))