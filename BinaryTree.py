from TreeNode import TreeNode as Node

class BinaryTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def getRoot(self):
        return self.root

    def setRoot(self, node):
        self.root = node

    def inOrderTraversal(self):
        return traverseInOrder(self.root)

    def __str__(self):
        return self.inOrderTraversal()

# helper method to recurse over nodes
# should only be called by inOrderTraversal class method above
def traverseInOrder(node):
    traversal = ""
    if (node == None):
        pass
    else:
        traversal += traverseInOrder(node.getLeftChild())
        traversal += node.getData() + "\n"
        traversal += traverseInOrder(node.getRightChild())
    return traversal
