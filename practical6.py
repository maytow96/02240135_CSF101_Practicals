#implimenting sorting algorithms
#inplace quick sort
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

#2.optimize bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

#3.hybrid sort
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    for i in range(left + 1, right):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_merge_sort(arr, threshold=10):
    if len(arr) <= 1:
        return arr
    if len(arr) < threshold:
        insertion_sort(arr)
        return arr

    mid = len(arr) // 2
    left = hybrid_merge_sort(arr[:mid])
    right = hybrid_merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

#4 visualisation with matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def visualize_sort(sorting_algorithm, arr):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) + 1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    operations = []

    def record_frame():
        operations.append(arr.copy())

    def quick_sort_visual(arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1
        if low < high:
            pi = partition_visual(arr, low, high)
            quick_sort_visual(arr, low, pi - 1)
            quick_sort_visual(arr, pi + 1, high)

    def partition_visual(arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                record_frame()
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        record_frame()
        return i

    if sorting_algorithm == "quick":
        quick_sort_visual(arr.copy())
    elif sorting_algorithm == "bubble":
        def bubble(arr):
            n = len(arr)
            for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        swapped = True
                        record_frame()
                if not swapped:
                    break
        bubble(arr.copy())

    def update_fig(A, rects):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        text.set_text(f"# Operations: {operations.index(A)}")

    ani = animation.FuncAnimation(
        fig, func=update_fig, fargs=(bar_rects,),
        frames=operations, interval=100, repeat=False
    )
    plt.show()

# Example usage
arr = random.sample(range(1, 50), 25)
visualize_sort("quick", arr)  # change to "bubble" to view bubble sort

#5.