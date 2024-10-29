import time
import random
import copy

# Timing function
def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr)
    end_time = time.time()
    return end_time - start_time

# Generate test arrays
def generate_test_arrays(size):
    best_case = list(range(size))         # Sorted in ascending order
    average_case = random.sample(range(size), size)  # Random order
    worst_case = list(range(size, 0, -1)) # Sorted in descending order
    return best_case, average_case, worst_case

# Sorting functions
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Analysis function
def analyze_algorithms(size):
    best_case, average_case, worst_case = generate_test_arrays(size)
    
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    results = {}
    for name, algorithm in algorithms.items():
        results[name] = {}
        
        for case_name, array in [("Best Case", best_case), 
                                 ("Average Case", average_case), 
                                 ("Worst Case", worst_case)]:
            arr_copy = copy.deepcopy(array)  # Clone array for consistent testing
            
            if name == "Quick Sort":
                start_time = time.time()
                arr_copy = quick_sort(arr_copy)
                exec_time = time.time() - start_time
            else:
                exec_time = time_sorting_algorithm(algorithm, arr_copy)
                
            results[name][case_name] = exec_time
            print(f"{name} - {case_name}: {exec_time:.6f} seconds")
            
    return results

# Run the analysis
size = 1000  # Example size
results = analyze_algorithms(size)

# Display results summary
for algo, cases in results.items():
    print(f"\n{algo}:")
    for case, exec_time in cases.items():
        print(f"  {case}: {exec_time:.6f} seconds")
