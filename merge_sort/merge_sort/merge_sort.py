def quick_sort(og_list , left = 0, right = None): 
    # left = 0
    # right = len(og_list) - 1

    if right is None: 
        right = len(og_list) - 1

    if left < right:
        position = partition(og_list, left, right)
        quick_sort(og_list, left, (position -1))
        quick_sort(og_list, (position + 1), right)

    print("OG", og_list)
    return og_list

def partition(og_list, left, right):
    pivot = og_list[right]
    low = left - 1 
    i = left

    while i < right:
        if og_list[i] <= pivot:
            low += 1
            swap_it(og_list, i, low)
        i += 1
    
    swap_it(og_list, right, low + 1)
    return low + 1

def swap_it(og_list, i, low):
    temp = og_list[i]
    og_list[i] = og_list[low]
    og_list[low] = temp

quick_sort([9, 11, 1, 5, 77, 4])
