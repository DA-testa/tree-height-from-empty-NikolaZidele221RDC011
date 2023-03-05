# python3

# import sys
# import threading
# import numpy


def compute_height(numbers, n):
    max_height = 0
    for i in range(n):
        indekss = i
        tagad = 1
        while numbers[indekss] != -1:
            tagad = tagad + 1
            indekss = numbers[indekss]
        max_height = max(max_height, tagad)
    return max_height


#def main():
if __name__ == '__main__':
    letter = input("Enter letter I or F: ")
    if letter == "I" or letter == "i":
        b = int(input())
        numbers = input()
        numbers = numbers.split()
        numbers = map(int, numbers)
        numbers = list(numbers)
        n = len(numbers)
        augstums = compute_height(numbers, n)
        print(augstums)
    elif letter == "F" or letter == "f":
        file = input()
        with open("./test/" + file, mode='r') as fails:
            b = fails.readline()
            numbers = fails.readline()
            numbers = numbers.split()
            numbers = map(int, numbers)
            numbers = list(numbers)
            n = len(numbers)
            augstums = compute_height(numbers, n)
            print(augstums)
    else:
        print("Next time enter I or F value!")


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
# sys.setrecursionlimit(10**7)  # max depth of recursion
# threading.stack_size(2**27)   # new thread will get stack of such size
# threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))
