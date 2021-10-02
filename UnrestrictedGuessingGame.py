# Hong Anh Nguyen - Assignment 6
# This program is an extention of GuessingGame, where user can pick a thing
#that is not on the pre-specified list

from TreeNode import TreeNode as Node
from BinaryTree import BinaryTree
from GuessingGame import GuessingGame
from GameTreeReader import GameTreeReader
import sys

class UnrestrictedGuessingGame(GuessingGame):
    def __init__(self, newTree):
        super().__init__(newTree)

    # getReady inherit from GuessingGame and expand the application
    ## Params:
    #       type (str): the type of program (restricted/unrestricted)
    # return boolean/None
    def getReady(self, type):
        check = super().getReady(type)
        # if type is unrestricted and self.current is an object
        if type == "unrestricted" and self.current != True and self.current != None:
            ques1 = input("What character were you thinking of? ")
            ques2 = input("Please give me a yes/no question that would distinguish your choice: ")
            ques3 = input("What is the answer to your question? [yes/no] ")
            val = self.current.getData()
            self.current.setData(ques2)
            # if the answer is yes
            if ques3 == "yes":
                self.current.setLeftChild(Node(ques1))
                self.current.setRightChild(Node(val))
            # if answer is no
            elif ques3 == "no":
                self.current.setLeftChild(Node(val))
                self.current.setRightChild(Node(ques1))
            print("Thank you! I have added " + ques1 + " to the game.\n")
        return check

# main use answers from input to call corresponding methods
def main():
    # create a BinaryTree object from input file
    newTree = GameTreeReader(sys.argv[1]).getTree()
    newGame = UnrestrictedGuessingGame(newTree)
    play = newGame.setUp()
    # if user want to play
    if play == True:
        ready = newGame.getReady("unrestricted")
        # if user ready
        if ready == True:
            replay = newGame.restart()
            # if user want replay
            while replay == True:
                newGame.present()
                check = newGame.getReady("unrestricted")
                if check == False:
                    replay = False
                else:
                    replay = newGame.restart()

if __name__ == '__main__':
    main()
