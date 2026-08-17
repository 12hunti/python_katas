def quick_sort(numbers: list) -> list:
    
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers[0]

    less_pivot = [x for x in numbers[1:] if x < pivot]
    greater_pivot = [x for x in numbers[1:] if x >= pivot]
    
    return quick_sort(less_pivot) + [pivot] + quick_sort(greater_pivot) 