"""
Name: Jim Farrell
Description:
3. Extend the buildParseTree function to handle mathematical expressions that do
not have spaces between every character.
4. Extend the buildParseTree and evaluate functions to handle boolean statements.
Remember that "not" is a unary operator, so this will complicate your code somewhat.
"""
from Stack import *
from BinaryTree import *

       
def buildParseTree(fpexp):
    """modified buildParsTree method to handle boolean operations"""
    fplist = tokenize(fpexp)
    #print(fplist)
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        #included and, or , not
        elif i not in ['+', '-', '*', '/', ')', 'and', 'or', 'not']:
            if i.isdigit():
                #"i" is a number
                currentTree.setRootVal(int(i))
            else:
                #"i" is not a number
                currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent
        #included and, or, not
        elif i in ['+', '-', '*', '/', 'and', 'or', 'not']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def tokenize(fpexp):
    """function to format tokenList from input expression fpexp"""
    tokenList=[]
    #variable to keep track of previous character
    prev = None
    #iterate through the list and break out the tokens
    for i in fpexp:
        #if the current character and previous character were numbers
        if i.isdigit() and tokenList[-1].isdigit():
            #append the individual sequential numbers  
            tokenList[-1]=tokenList[-1]+i
            prev = "num"
        #case where current and previous were letters
        #using prev to separate boolean and,or,not from just letters to prevent (a and b) becoming aandb
        elif i.isalpha() and prev == "alpha":
            #append the letters
            tokenList[-1]=tokenList[-1]+i
            prev = "alpha"
        elif i.isspace():
            prev = " "
        #Either a single variable letter or start of logical operator
        elif i.isalpha():
            prev = "alpha"
            tokenList.append(i)
        else:
            tokenList.append(i)
            prev = None
    return tokenList

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())
      
def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal


def noSpaceTest():
    #expression with no spaces
    noSpaces = "((7+3)*(5-2))"
    numParseTree = buildParseTree(noSpaces)
    print("No Space test expression.", noSpaces)
    print("buildParseTree printexp..", printexp(numParseTree))
    print("\n-----inorder-----")
    inorder(numParseTree)
    
def boolStatementTest():
    #expression containing logical operators
    boolStatement = "(not((a and b)or(b and c)))"
    boolParseTree = buildParseTree(boolStatement)
    print("boolean test expression..", boolStatement)
    print("buildParseTree printexp..", printexp(boolParseTree))
    print("\n-----inorder-----")
    inorder(boolParseTree)

def runTests():
    print("\nTesting with no space in expression")
    noSpaceTest()
    print("\nTesting boolean statement")
    boolStatementTest()
    
runTests()


