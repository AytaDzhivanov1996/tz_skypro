def moving_zeros(array):
    new_array = sorted(array, key=lambda n: n == 0)
    return new_array


def get_sum_odd(n):
    summa = 0
    start = n**2 - (n - 1)
    end = start + n * 2
    for i in range(start, end, 2):
        summa += i
    return summa

