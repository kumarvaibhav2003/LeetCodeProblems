# Python program to sort an integer arrat using bubble sort

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all the elements of the array
    for i in range (n):
        swapped = False

        # Last element are already in place
        for j in range(0, n-i-1):
            # swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

if __name__ == "__main__":
    arr = [65, 34, 56, 12, 23, 97]
    print('Original Array:', arr)
    bubble_sort(arr)
    print('Sorted Array:', arr)