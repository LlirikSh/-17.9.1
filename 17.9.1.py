chislo = [int(x) for x in input("Введите числа через пробел в интервале от 1 до 500, затем нажмите enter: ").split()]
def merge_sort(chislo):  # "разделяй"
    if len(chislo) < 2:  # если кусок массива равен 2,
        return chislo[:]  # выходим из рекурсии
    else:
        middle = len(chislo) // 2  # ищем середину
        left = merge_sort(chislo[:middle])  # рекурсивно делим левую часть
        right = merge_sort(chislo[middle:])  # и правую
        return merge(left, right)  # выполняем слияние
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
print(merge_sort(chislo))

while True:
    try:
        element = int(input("Введите любое число: "))
        if element < 0 or element > 500:
            raise Exception
        break
    except ValueError:
        print("Введите число!")
    except Exception:
        print("Введите число от 1 до 500!")

def search(chislo, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if chislo[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < chislo[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return search(chislo, element, left, middle - 1)
    else:  # иначе в правой
        return search(chislo, element, middle + 1, right)

print(search(chislo, element, 0, len(chislo)))
