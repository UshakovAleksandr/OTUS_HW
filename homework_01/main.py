"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(lst_of_int_numbers):
    pow_nums = [i ** 2 for i in lst_of_int_numbers]
    return pow_nums


def is_prime(lst_of_int_numbers):
    prime_lst = []
    for i in lst_of_int_numbers:
        k = 0
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                k = k + 1
        if k <= 0:
            prime_lst.append(i)
    return prime_lst


def filter_numbers(lst_of_int_numbers, type_of_filter):
    if type_of_filter == "odd":
        odd_lst = list(filter(lambda x: x % 2 != 0, lst_of_int_numbers))
        return odd_lst
    if type_of_filter == "even":
        odd_lst = list(filter(lambda x: x % 2 == 0, lst_of_int_numbers))
        return odd_lst
    if type_of_filter == "prime":
        prime_lst = is_prime(lst_of_int_numbers)
        return prime_lst


def main():
    ODD = "odd"  # нечетные
    EVEN = "even"  # четные
    PRIME = "prime"  # простые
    lst = [1, 2, 4, 5, 7, 11, 14, 23, 30, 34, 45, 56]
    print(f"Массив квадратов чисел: {power_numbers(lst)}")
    print(f"Массив нечетных чисел: {filter_numbers(lst, ODD)}")
    print(f"Массив четных чисел: {filter_numbers(lst, EVEN)}")
    print(f"Массив простых чисел: {filter_numbers(lst, PRIME)}")


if __name__ == '__main__':
    main()