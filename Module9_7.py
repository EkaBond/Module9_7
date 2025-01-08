def is_prime(func):   #декоратор, примет на себя функцию sum_three, а вернет ф-ю wrapper
    def wrapper(*args): #можно добавить **kwargs, чтобы захватить именованные аргументы, т.к. в задании их нет, не стала ставить
        a = func(*args) #вызываю ф-ю sum_three и в переменную "а" сохраняю результат ф-ии
        counter = 0 #счетчик для результата цикла for
        for i in range(1, a + 1): #перебираю значения от 1 по результат sum_three включительно
            if a % i  == 0: # если остаток от деления ноль, то увеличиваю counter
                counter += 1
        if counter == 2: #если счетчик равен 2, то число делиться на 1 и себя. значит простое.
            print('Простое')
        else: print ('Составное')

        return a #возвращаем результат ф-и sum_three
    return wrapper



@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

