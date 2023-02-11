def my_special_sort (nums):
    for i in range(1, len(nums)):
        a = nums[i]
        idx = i
        while idx > 0 and nums[idx-1] > a:
            nums[idx] = nums[idx-1]
            idx -= 1
        nums[idx] = a
    return nums

def binary_search(array, element, left, right ):

    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element and array[middle-1] < element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс
    elif element > array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в правой половине
        return binary_search(array, element, middle + 1, right)
    else:  # иначе в левой
        return binary_search(array, element, left, middle - 1)

x = []
with open('array.txt', 'r') as file:
    # Получаем все строки из файла
    lines = file.readlines()

for line in lines:
    temp = line.split()
    x.extend(temp)
print(x)

nums = list(map(float, x))
print(nums)

sorted_nums = my_special_sort(nums)
print(sorted_nums)

# ввод пользовательских данных
new_num = input(f"Введите число больше {sorted_nums[0]} и меньше или равное {sorted_nums[-1]}:")
try:
    new_num = float(new_num)
    if new_num > sorted_nums[0] and new_num <= sorted_nums[-1]:
        nums.append(new_num)
        sorted_nums = my_special_sort(nums)
        y = binary_search(sorted_nums, new_num, 0, len(sorted_nums) - 1)
        print(f"индекс запрашиваемого элемента  {y}")
    else:
        print("Введенное число за пределами указанного диапазона")
except:
    print("Некорректный ввод данных")