
from math import floor


print("Algorithm Sorter")
numbers = []
while True:
    print("[1] Add set of numbers")
    print("[2] Choose algorithm methods and calculate")
    print("[3] Reset numbers")
    print("[4] Show numbers")
    print("[5] Quit")
    menu1 = input()

    if menu1 == "1":
        input_string = input("Enter a list elements separated by space ")

        print("\n")
        stringnumbers = input_string.split()
        numbers = [float(i) for i in stringnumbers]

        print("user list is ", numbers)

    elif menu1 == "2":
        print("Choose an algorithm method:")
        print("[1] bubble sort")
        print("[2] insertion sort")
        print("[3] shell sort")
        print("[4] merge sort")
        print("[5] bucket sort")
        print("[6] radix sort")
        print("[7] selection sort")
        print("[8] quick sort")
        print("[x] back")
        algo = input()
        if algo == 1:
            # bubble_sort

            def bubble_sort(numbers):
                print("Process:")
                for i in range(len(numbers) - 1, 0, -1):

                    print(str(numbers))
                    for j in range(i):

                        if numbers[j] > numbers[j + 1]:
                            temporary = numbers[j]

                            numbers[j] = numbers[j + 1]

                            numbers[j + 1] = temporary


            bubble_sort(numbers)

            print("\nSorted List using Bubble Sort:\n" + str(numbers))



        elif algo == 2:
            # insertion_sort

            def insertion_sort(numbers):
                print("Process:")
                indexing_length = range(1, len(numbers))

                for i in indexing_length:
                    print(str(numbers))
                    value_to_sort = numbers[i]

                    while numbers[i - 1] > value_to_sort and i > 0:
                        numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]

                        i = i - 1

                return numbers


            insertion_sort(numbers)
            print("\nSorted List using Insertion Sort:\n" + str(numbers))


        elif algo == 3:
            # shell_sort

            def shellSort(numbers):
                print("Process:")
                n = len(numbers)
                gap = floor(n / 2)
                while gap > 0:
                    for i in range(gap, n):
                        print(str(numbers))
                        temp = numbers[i]
                        j = i
                        while j >= gap and temp < numbers[j - gap]:
                            numbers[j] = numbers[j - gap]
                            j -= gap
                        numbers[j] = temp
                    gap = floor(gap / 2)


            shellSort(numbers)
            print("\nSorted List using Shell Sort:\n" + str(numbers))

        elif algo == 4:
            # merge_sort

            def mergeSort(numbers):
                print("Process:")
                print(str(numbers))
                if len(numbers) > 1:
                    mid = len(numbers) // 2
                    left = numbers[:mid]
                    right = numbers[mid:]
                    mergeSort(left)
                    mergeSort(right)
                    i = 0
                    j = 0
                    k = 0

                    while i < len(left) and j < len(right):
                        if left[i] < right[j]:
                            numbers[k] = left[i]
                            i += 1
                        else:
                            numbers[k] = right[j]
                            j += 1
                        k += 1
                    while i < len(left):
                        numbers[k] = left[i]
                        i += 1
                        k += 1
                    while j < len(right):
                        numbers[k] = right[j]
                        j += 1
                        k += 1


            mergeSort(numbers)
            print("\nSorted List using Merge Sort:\n" + str(numbers))

        elif algo == 5:
            # bucket_sort
            print("Process:")


            def insertion(inpvalue):
                print(str(inpvalue))
                for i in range(1, len(inpvalue)):
                    temp = inpvalue[i]
                    j = i - 1
                    while (j >= 0 and temp < inpvalue[j]):
                        inpvalue[j + 1] = inpvalue[j]
                        j = j - 1
                    inpvalue[j + 1] = temp


            def bucket_sort(inpvalue):

                largest = max(inpvalue)
                length = len(inpvalue)
                size = largest / length

                buckets = [[] for _ in range(length)]
                for i in range(length):

                    j = int(inpvalue[i] / size)

                    if j != length:
                        buckets[j].append(inpvalue[i])
                    else:
                        buckets[length - 1].append(inpvalue[i])

                for i in range(length):
                    insertion(buckets[i])

                res = []

                for i in range(length):
                    res = res + buckets[i]

                return res


            inpvalue = numbers

            sorted_list = bucket_sort(inpvalue)
            print("\nSorted List using Bucket Sort: ", end='')
            print(sorted_list)


        elif algo == 6:
            # radix_sort
            def countingSort(array, place):
                print("Process:")
                size = len(array)
                output = [0] * size
                count = [0] * 10
                for i in range(0, size):
                    index = array[i] // place
                    count[index % 10] += 1
                for i in range(1, 10):
                    count[i] += count[i - 1]
                i = size - 1
                while i >= 0:
                    index = array[i] // place
                    output[count[index % 10] - 1] = array[i]
                    count[index % 10] -= 1
                    i -= 1
                for i in range(0, size):
                    array[i] = output[i]


            def radixSort(array):

                max_element = max(array)

                place = 1

                while max_element // place > 0:
                    countingSort(array, place)

                    place *= 10


            data = numbers
            radixSort(data)
            print("\nSorted List using Radix Sort:\n" + str(data))


        elif algo == 7:
            # selection_sort
            print("Process:")


            def selection_sort(numbers):

                indexing_length = range(0, len(numbers) - 1)

                for i in indexing_length:
                    print(str(numbers))
                    min_value = i

                    for j in range(i + 1, len(numbers)):

                        if numbers[j] < numbers[min_value]:
                            min_value = j

                    if min_value != i:
                        numbers[min_value], numbers[i] = numbers[i], numbers[min_value]

                return numbers


            selection_sort(numbers)
            print("\nSorted List using Selection Sort:\n" + str(numbers))
        elif algo == 8:
            # quick_sort
            print("Process:")


            def quick_sort(numbers):
                length = len(numbers)
                print(str(numbers))
                if length <= 1:

                    return numbers
                else:
                    pivot = numbers.pop()
                items_greater = []
                items_lower = []
                for item in numbers:

                    if item > pivot:
                        items_greater.append(item)
                    else:
                        items_lower.append(item)

                return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


            print("\nSorted List using Quick Sort:\n" + str(quick_sort(numbers)))

    elif menu1 == "3":
        numbers = []
        print("List value reset successfully...")

    elif menu1 == "4":

        if numbers == []:
            print("No numbers added yet...")
        else:
            print("List of numbers: ")
            print(numbers)


    elif menu1 == '5':
        print("Exiting program...")
        menu1 = ''
        quit()

    else:
        print("Invalid choice...")






