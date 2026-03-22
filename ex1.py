import random

num_list: list[int] = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
n: int = random.randint(1, 5)
def n_th_biggest_number(list: list[int], n: int) -> int:
    list = set(list)
    for i in range(n - 1):
        list.remove(max(list))
    return max(list)
print(n)
print(n_th_biggest_number(num_list, n))