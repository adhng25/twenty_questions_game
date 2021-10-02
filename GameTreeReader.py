from BinaryTree import BinaryTree
from TreeNode import TreeNode
import sys

class GameTreeReader():
	def __init__(self, filename):
		self.tree = BinaryTree()
		tf = open(filename, "r")
		self.allLines = tf.readlines()
		tf.close()
		self.tree.root = self.parseFileRecursively()

	def parseFileRecursively(self):
		#start with the first line
		line = self.allLines[0]
		tabCount = line.count("\t")
		node = TreeNode(line[tabCount:len(line)-1])
		#remove the first line
		self.allLines = self.allLines[1:]
		#if we've got enough left for two children
		if len(self.allLines) > 1:
			line = self.allLines[0]
			if line.count("\t") > tabCount:
				node.setLeftChild(self.parseFileRecursively())
				#previous line was deleted in the recursion, so don't delete another
				line = self.allLines[0]
				node.setRightChild(self.parseFileRecursively())
		return node

	def getTree(self):
		return self.tree

# To use:
# newTree = GameTreeReader(file name goes here).getTree()
