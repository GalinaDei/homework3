# Задание 1
# ✔ Дан список повторяющихся элементов. Вернуть список  с дублирующимися элементами. В результирующем списке не
# #должно быть дубликатов.


lst = [1, 1, 2, 1, 'One', 10, 5, 'Two', 'One', 1, 5, 'Two', (2, 3), True, False, False, False, False, 1]


def find_duplicates(lst) -> list:
    st = set(lst)
    st1 = set()
    for elem in st:
        if lst.count(elem) > 1:
            st1.add(elem)
    return(list(st1))


print(find_duplicates(lst))



