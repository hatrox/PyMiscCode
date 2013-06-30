#!/bin/python

def readInput(count):
  list = []
  for i in range(0, count):
    item = int(raw_input('list[' + str(i) + '] = '))
    list.append(item)
  
  return list

def nacci(numbers, index):
  assert 0 < index, 'Index must be positive!'

  if 0 < index and index < len(numbers):
    return numbers[index]

  index -= len(numbers)
  count = len(numbers)
  for i in range(0, index):
    nextMember = 0
    for j in range(len(numbers) - count, len(numbers)):
      nextMember += numbers[j]
    
    numbers.append(nextMember)
    numbers = numbers[1:]
  
  return numbers[len(numbers) - 1]

count = int(raw_input('Enter count: '))
list = readInput(count)

n = int(raw_input('Which member? '))
print nacci(list, n)

# we all know every next member of the fibonacci sequence is calculated by the sum of the previous two members,
# the next members of the tribonacci sequence are generated by the sum of the previous three, the quadronacci - 
# by the sum of the previous four and so on. this program can calculate any member of a n-nacci sequence, given
# the first n members
