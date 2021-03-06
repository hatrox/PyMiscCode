#!/bin/python

def printVariations(numbers, index, limit):
  if index == len(numbers):
    print numbers
    return
  
  for i in range(1, limit + 1):
    numbers[index] = i
    printVariations(numbers, index + 1, limit)

def initializeList(list, count):
  for i in range(0, count):
    list.append(0)

count = int(raw_input('Enter count: '))
limit = int(raw_input('Enter range: '))

numbers = []
initializeList(numbers, count)

printVariations(numbers, 0, limit)

# an extremely simple recursive algorithm, which will print out every variation
# from 1 to N (range/limit), for k numbers (count)
# I know this probably isn't the best way to initialize a list with a length of n
# in Python, but it works well enough for this case
