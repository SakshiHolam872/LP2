def greedy_selection_sort(arr): 
    n = len(arr) 
 
    for i in range(n): 
        # Find the minimum element in the unsorted part 
        min_index = i 
        for j in range(i + 1, n): 
            if arr[j] < arr[min_index]: 
                min_index = j 
 
        # Swap the found minimum element with the first element 
        arr[i], arr[min_index] = arr[min_index], arr[i] 
 
    return arr 
 
# Example usage: 
#input_array = [64, 25, 12, 22, 11] 

arr= input("Enter the list of numbers: ").split()
arr= [int(x) for x in arr]

sorted_array = greedy_selection_sort(arr) 
print("Sorted array:", sorted_array)





















#Selection sort is a simple comparison-based sorting algorithm that divides the input array into two parts: a sorted part and an unsorted part. 

# Here's a step-by-step explanation of the selection sort algorithm:

# Start with an unsorted array of n elements.
# Find the minimum (or maximum) element in the unsorted part of the array.
# Swap the minimum (or maximum) element with the first element of the unsorted part.
# Move the boundary of the sorted part one element to the right.
# Repeat steps 2-4 until the entire array is sorted.


