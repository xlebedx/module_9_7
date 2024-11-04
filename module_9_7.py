def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        summ = sum(args)
        c = 0
        for i in range(2, summ // 2 + 1):
            if summ % i == 0:
                c = c + 1
        if c <= 0:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
