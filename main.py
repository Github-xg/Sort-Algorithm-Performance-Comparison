import time
import random

def quick_sort(arr):
    # 快速排序的递归函数
    def sort(low, high):
        # 如果数组为空或只包含一个元素，则不需要排序
        if low >= high:
            return
        # 取第一个元素作为基准元素
        pivot = arr[low]
        # 初始化交换次数、比较次数、移动次数
        Q_swap_count = 0
        Q_compare_count = 0
        Q_move_count = 0
        # 使用双指针法将数组分为两部分
        i, j = low, high
        while i < j:
            # 从后往前扫描，找到第一个小于等于基准元素的元素
            while i < j and arr[j] > pivot:
                j -= 1
                Q_compare_count += 1
            # 将该元素移动到左半部分
            if i < j:
                arr[i] = arr[j]
                i += 1
                Q_move_count += 1
                Q_swap_count += 1
            # 从前往后扫描，找到第一个大于基准元素的元素
            while i < j and arr[i] <= pivot:
                i += 1
                Q_compare_count += 1
            # 将该元素移动到右半部分
            if i < j:
                arr[j] = arr[i]
                j -= 1
                Q_move_count += 1
                Q_swap_count += 1
        # 将基准元素移动到数组的中间位置
        arr[i] = pivot
        Q_move_count += 1
        # 递归地对左右两部分进行排序
        sort(low, i - 1)
        sort(i + 1, high)
        return Q_swap_count, Q_compare_count, Q_move_count

    n = len(arr)
    # 记录开始时间
    start_time = time.perf_counter()
    # 调用递归函数进行快速排序
    Q_swap_count, Q_compare_count, Q_move_count = sort(0, n - 1)
    # 记录结束时间
    end_time = time.perf_counter()
    # 计算排序所用时间
    elapsed_time = end_time - start_time
    # 打印结果
    print("快速排序所需的交换次数：", Q_swap_count)
    print("快速排序所需的比较次数：", Q_compare_count)
    print("快速排序所需的移动次数：", Q_move_count)
    print(f"快速排序所需的排序时间： {elapsed_time:.5f}\n")

def selection_sort(arr):
    start_time = time.perf_counter()
    swap_count = 0
    compare_count = 0
    move_count = 0

    for i in range(len(arr)):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, len(arr)):
            compare_count += 1
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part
        swap_count += 1
        move_count += 3
        arr[i], arr[min_index] = arr[min_index], arr[i]

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # 打印结果
    print("选择排序所需的交换次数：", swap_count)
    print("选择排序所需的比较次数：", compare_count)
    print("选择排序所需的移动次数：", move_count)
    print(f"选择排序所需的排序时间： {elapsed_time:.5f}\n")
    return (elapsed_time, swap_count, compare_count, move_count)

def insertion_sort(arr):
    # 记录交换次数、比较次数、移动次数
    swaps = 0
    comparisons = 0
    movements = 0
    start_time = time.perf_counter()

    for i in range(1, len(arr)):
        j = i
        # 寻找合适的位置进行插入
        while j > 0 and arr[j] < arr[j - 1]:
            # 交换两个数的位置
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swaps += 1
            movements += 3
            j -= 1
            comparisons += 1
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # 打印结果
    print("插入排序所需的交换次数：", swaps)
    print("插入排序所需的比较次数：", comparisons)
    print("插入排序所需的移动次数：", movements)
    print(f"插入排序所需的排序时间： {elapsed_time:.5f}\n")

    return swaps, comparisons, movements

def merge_sort(lst):
    # 交换、比较、移动的次数
    swaps = 0
    comparisons = 0
    movements = 0

    if len(lst) <= 1:
        return lst, swaps, comparisons, movements

    # 将列表分成两半
    half = len(lst) // 2
    left = lst[:half]
    right = lst[half:]

    # 对两半进行归并排序
    left, swaps, comparisons, movements = merge_sort(left)
    swaps += swaps
    comparisons += comparisons
    movements += movements
    right, swaps, comparisons, movements = merge_sort(right)
    swaps += swaps
    comparisons += comparisons
    movements += movements
    # 将两半合并起来
    return merge(left, right, swaps, comparisons, movements)

def merge(left, right, swaps, comparisons, movements):
    result = []

    # 归并两个列表
    while left and right:
        # 比较两个列表的首个元素
        comparisons += 1
        if left[0] < right[0]:
            result.append(left.pop(0))
            movements += 1
        else:
            result.append(right.pop(0))
            movements += 1
            swaps += 1

    # 将剩余部分加入结果列表
    result.extend(left)
    result.extend(right)
    movements += len(left) + len(right)
    return result, swaps, comparisons, movements
# 测试
arr = [random.randint(1, 100000) for i in range(1000)]
arr2=[None] * len(arr)
for i in range(0, len(arr)):
    arr2[i] = arr[i]
arr3=[None] * len(arr)
for i in range(0, len(arr)):
    arr3[i] = arr[i]
arr4=[None] * len(arr)
for i in range(0, len(arr)):
    arr4[i] = arr[i]
print(f'排序的数据有{len(arr)}个')

quick_sort(arr)
selection_sort(arr2)
insertion_sort(arr3)
start_time = time.perf_counter()
result, swaps, comparisons, movements = merge_sort(arr4)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
# 打印结果
print("归并排序所需的交换次数：", swaps)
print("归并排序所需的比较次数：", comparisons)
print("归并排序所需的移动次数：", movements)
print(f"归并排序所需的排序时间： {elapsed_time:.5f}\n")
print(arr)

