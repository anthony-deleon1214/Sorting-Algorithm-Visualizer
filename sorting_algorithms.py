# Implementation of various sorting algorithms
# Each algorithm will be implemented as a function
# There is also a function to generate a random array

import random

def rand_array(size: int=50) -> list:
    """
    Populates an array of input size with random values between 1 and 100
    Returns the populated array
    """
    output_list = []
    for i in range(0, size):
        output_list.append(random.randint(1, 100))
    return output_list

def bubble_sort(input_list: list) -> None:
    """
    Sorts the input_list in place using the bubble sort algorithm
    Currently sorts in ascending order
    """
    last_index = len(input_list)-1                                                      # Track last unsorted index
    while last_index >= 1:                                                              # Loop until last unsorted index is 0
        for i in range(0, last_index):                                                  # Loop from start to last unsorted
            if input_list[i] > input_list[i+1]:                                         # Compare element to next element
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]         # Swap if first element is greater
        last_index -= 1                                                                 # Decrement last_index counter

def insertion_sort(input_list: list) -> None:
    """
    Sorts the input list in place using insertion sort
    Sorts in ascending order
    """
    for i in range(1, len(input_list)):                                                 # Iterate through list starting from index 1
        if input_list[i] < input_list[i-1]:                                             # If item at index i is less than previous element
            input_list[i], input_list[i-1] = input_list[i-1], input_list[i]             # Swap the two elements
            j = i-1                                                                     # Initialize a separate counter
            while j > 0 and input_list[j] < input_list[j-1]:                            # Iterate backwards swapped element is still greater than previous element
                input_list[j], input_list[j-1] = input_list[j-1], input_list[j]         # Swap if necessary
                j -= 1

def selection_sort(input_list: list) -> None:
    """
    Sorts input list in place using selection sort
    Sorts in ascending order
    """
    min_index = 0
    for i in range(0, len(input_list)):
        current_min = input_list[min_index]
        for j in range(min_index+1, len(input_list)):
            if input_list[j] < current_min:
                pass


def cocktail_sort(input_list: list) -> None:
    """
    Sorts input list in ascending order using cocktail sort
    """
    first_index = 0
    last_index = len(input_list)-1
    swaps_made = False
    while not swaps_made:
        for i in range(first_index, last_index):                                        # Forward pass (identical to bubble sort)
            if input_list[i] > input_list[i+1]:
                input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
                swaps_made = True
        last_index -= 1                                                                 # Decrement last_index
        for j in range(last_index, first_index, -1):                                    # Backwards pass
            if input_list[j] < input_list[j-1]:
                pass

def quicksort(input_list: list) -> None:
    """
    Passes the input list to the quicksort helper function
    Eases calling quicksort for end user
    """
    quicksort_helper(input_list, 0, len(input_list)-1)

def quicksort_helper(input_list: list, low: int, hi: int) -> None:
    """
    Sorts input list in place using quick sort
    Pivot is chosen as the middle of the subarray
    """
    if low >= 0 and hi >= 0 and low < hi:
        pivot = partition(input_list, low, hi)
        quicksort_helper(input_list, low, pivot)
        quicksort_helper(input_list, pivot+1, hi)

    
def partition(input_list: list, low: int, hi: int) -> int:
    """
    Partitions the input list using low and hi pointers
    Defines a pivot point based on the low and hi pointers
    Increments pointers and compares the values at each pointer location
    Swaps the values if necessary
    Returns the position where the pointers meet
    """
    pivot_index = (hi+low)//2
    pivot_val = input_list[pivot_index]
    i = low - 1
    j = hi + 1
    while True:
        i += 1
        while input_list[i] < pivot_val:
            i += 1
        j -= 1
        while input_list[j] > pivot_val:
            j -= 1
        if i >= j:
            return j
        input_list[i], input_list[j] = input_list[j], input_list[i]

# Test print statements
test_list = rand_array(25)
print("Input list: " + str(test_list))
quicksort(test_list)
print("Sorted list: " + str(test_list))