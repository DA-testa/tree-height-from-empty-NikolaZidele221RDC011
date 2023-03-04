# python3

import sys
import threading
# import numpy


def compute_height(n, numbers):
    max_height = 0
    for i in range(n):
        indekss = int(i)
        tagad = 1
        while (numbers[int(indekss)] != -1):
            tagad = tagad + 1
            indekss = int(numbers[indekss])
        max_height = max(max_height, tagad)
    return max_height


def main():
    letter = str(input("I or F: "))
    if letter == "I" or letter == "i":
        n = int(input())
        numbers = input()
        numbers = numbers.split()
        compute_height(n, numbers)
        print(compute_height(n, numbers))
    elif letter == "F" or letter == "f":
        file = input()
        with open("./test/" + file, mode='r') as fails:
            n = fails.readline()
            numbers = fails.readline()
            numbers = numbers.split()
        compute_height(n, numbers)
        print(compute_height(n, numbers))
    else:
        print("Ievadiet I vai F rakstzīmi: ")
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))