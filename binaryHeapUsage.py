"""
Name: Jim Farrell
Description:
1. Generate a random list of integers.  
Show the binary heap tree resulting from inserting the integers on the list one at a time.
2. Using the list from the previous question, show the binary heap tree resulting from the list
as a parameter to the buildHeap method.  Section 6.6.1 PG 269
Show both the tree and list form.
"""

from random import *
from binaryHeap import *

def showTree(items):
    """function to print tree"""
    print("{0:>20}".format(items[1]))
    print()
    print("{0:>18}{1:>4}".format("/", " \\" ))
    print()
    print("{0:16}{1:>9}".format(items[2 * 1], items[2 * 1 + 1]))
    print()
    print("{0:>14}{1:>4}{2:>5}{3:>4}".format("/", " \\", "/", " \\" ))
    print()
    print("{0:>12}{1:7}{2:>3}{3:>7}".format(items[2 * 2], items[2 * 2 + 1],items[2 * 3], items[2 * 3 + 1]))
    print()
    print("{0:>10}{1:>4}".format("/", " \\" ))
    print()
    print("{0:>9}{1:>7}".format(items[2 * 4], items[2 * 4 + 1]))

def testOneAtATime(randomList):
    """function to test inserting integers one at a time"""
    binHeap1 = BinaryHeap()
    print("Random List = ", randomList)
    print("------------One at a time----------------")
    for i in range(9):
        binHeap1.insert(randomList[i])
    showTree(binHeap1.getResults())

def testWithList(randomList):
    """function to test using list as a parameter to buildHeap method"""
    binHeap2 = BinaryHeap()
    print("Random List = ", randomList)
    print("-----------Passed as a list--------------")
    binHeap2.buildHeap(randomList)
    showTree(binHeap2.getResults())

def runTest():
    """Run the test examples"""
    #generate a random list of numbers between 1 and 99 of length 9
    randomList = sample(range(1,100), 9)
    
    testOneAtATime(randomList)
    testWithList(randomList)
    
runTest()
    


