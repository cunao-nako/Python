def binarySearch(my_list, item):
    if item not in my_list:
        return 'К сожалению данного элемента нет в списке.'
    my_list.sort()
    i = 1
    low = my_list[0]
    high = len(my_list) + 1
    while low <= high:
        mid = (low + high) // 2
        if mid == item:
            return(f'Алгоритм завершилась за {i} шагов.\n' +
                   f'Позиция {item} = {my_list.index(mid) + 1}.')
        elif item > mid:
            low = mid
        elif item < mid:
            high = mid
        i += 1


if __name__ == "__main__":
    print('Программа запущенна.')
    my_list = [i for i in range(1, 100001)]
    print(binarySearch(my_list, int(input('Введите запрос: '))))
