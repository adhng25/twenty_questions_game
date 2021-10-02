# Hong Anh Nguyen - Assignment 6
# 2 new methods is added to TreeNode class

class TreeNode:
    def __init__(self, data):
        self.leftChild = None
        self.rightChild = None
        self.data = data

    def getData(self):
        return self.data

    def setData(self, newValue):
        self.data = newValue

    def getLeftChild(self):
        return self.leftChild

    def setLeftChild(self, node):
        self.leftChild = node

    def getRightChild(self):
        return self.rightChild

    def setRightChild(self, node):
        self.rightChild = node

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild() == None

    def __str__(self):
        return str(self.data)

    # getLeaf gets all the leaves and prints them
    # Params: None
    # return None
    def getLeaf(self):
        if self.isLeaf():
            print(self.getData())
        else:
            self.getLeftChild().getLeaf()
            self.getRightChild().getLeaf()

    # display check if the program guess correctly
    # Params: None
    # return boolean/object
    def display(self):
        if self.isLeaf():
            query = input("Was you thinking of " + self.getData() + "? ")
            # if guess correct
            if query == "yes":
                return True
            # if not
            return self

        query = input(self.getData() + " ")
        # traverse through the tree
        if query == "yes":
            return self.getLeftChild().display()
        elif query == "no":
            return self.getRightChild().display()
        else:
            return self.display()
