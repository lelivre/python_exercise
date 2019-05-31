from __future__ import print_function

def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneuous
    comparable items inside
    :return: the same collection ordered by ascending
    """

    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1]=collection[j+1], collection[j]
        if not swapped: break # Stop iteration if the collection is sorted.
    return collection

if __name__ == '__main__':
    try:
        raw_input  #Python 2
    except NameError:
        raw_input = input # Python 3

    user_input = raw_input('Enter numbers separated by a comma:').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(*bubble_sort(unsorted), sep=',')
