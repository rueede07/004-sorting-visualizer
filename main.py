def bubble_sort(numbers):
    
    n = len(numbers)
    for pass_number in range(n):
        swapped = False

        # Largest value is moved to the end after every loop
        # After n times, list is sorted. Therefore range(n).

        for i in range(n - 1):
            
            if numbers[i] > numbers[i + 1]:
                print(f"Swapped {numbers[i]} with {numbers[i+1]}")
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

                swapped = True
                print(numbers)
        if not swapped:
            break

    return numbers

def selection_sort(numbers: list):
    n = len(numbers)

    for j in range(n):
        smallest_index = j

        for i in range(j + 1, n):
            if numbers[i] < numbers[smallest_index]:
                smallest_index = i
        
        if smallest_index !=j:
            print(f"Swapped {numbers[j]} with {numbers[smallest_index]}")
            numbers[j], numbers[smallest_index] = numbers[smallest_index], numbers[j]
            print(numbers)

    return f"Sorted list: {numbers}"
print(selection_sort([1, 23, 7, 5,23,23]))