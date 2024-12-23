#Задача "Всё не так уж просто":
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)):
    if numbers[i] == 1: # 1 не является ни простым, ни составным числом
        continue
    elif numbers[i] == 2: # Число 2 простое, влож цикл не будет проверять последовательность начиная с 2
        primes.append(numbers[i])
    else:
        for j in range(2, numbers[i]):
            if numbers[i] != j and numbers[i] % j == 0: #and numbers[i] / j > 1:
                #print(numbers[i])
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime == True:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
print('Not primes:', not_primes)
print('Primes:', primes)