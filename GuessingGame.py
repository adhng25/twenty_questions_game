# Hong Anh Nguyen - Assignment 6
# This program imitates the 20 Questions game. In this version of the game,
#the human thinks of something and the computer will try to guess it.

from TreeNode import TreeNode as Node
from BinaryTree import BinaryTree
from GameTreeReader import GameTreeReader
import sys

class GuessingGame:
    '''
    GuessingGame

    Instance variables:
        root
        current
    '''

    def __init__(self, newTree):
        self.root = newTree.getRoot()
        self.current = None

    # present prints all the leaves to console
    # Params: None
    # return None
    def present(self):
        print("Here is the guessing list:\n")
        self.root.getLeaf() # function getLeaf from TreeNode
        print("")

    # setUp introduce the game to user
    # Params: None
    # return boolean
    def setUp(self):
        prompt = input("Welcome to the Guessing game! Do you want to try it out? [yes/no] ")
        bool = False
        while bool == False:
            # if user want to play
            if prompt == "yes":
                self.present()
                bool = True
                return True
            # if not want to play
            elif prompt == "no":
                print("Okay, see you next time!")
                bool = True
            # if user enter wrong command
            else:
                print("Sorry I do not get that. Please try again.")
                prompt = input("Welcome to the Guessing game! Do you want to try it out? [yes/no] ")

    # getReady check if user ready and run the program
    # Params:
    #       type (str): the type of program (restricted/unrestricted)
    # return boolean/None
    def getReady(self, type):
        prompt = input("Choose one and I will guess it. Are you ready? [yes/no] ")
        bool = False
        while bool == False:
            # if user ready
            if prompt == "yes":
                print("Let's start. Please answer yes or no to the following questions.\n")
                self.current = self.root.display()  # call display method from TreeNode
                # if the guess was correct
                if self.current == True:
                    print("Yes! I got it right.\n")
                # if the guess was wrong
                elif type == "restricted":
                    print("I got it wrong?\n")
                bool = True
                return True
            # if user not ready
            elif prompt == "no":
                print("Okay, see you next time!")
                bool = True
            # if enter wrong command
            else:
                print("Sorry I do not get that. Please try again.")
                prompt = input("Choose one and I will guess it. Are you ready? [yes/no] ")

    # restart check if user want to play again
    # Params: None
    # return boolean/None
    def restart(self):
        prompt = input("Do you wanna play again? [yes/no] ")
        bool = False
        while bool == False:
            # if user want to replay
            if prompt == "yes":
                bool = True
                return True
            # if refuse
            elif prompt == "no":
                print("Okay, see you next time!")
                bool = True
            # wrong command
            else:
                print("Sorry I do not get that. Please try again.")
                prompt = input("Do you wanna play again? [yes/no] ")

# main use answers from input to call corresponding methods
def main():
    # create a BinaryTree object from input file
    newTree = GameTreeReader(sys.argv[1]).getTree()
    newGame = GuessingGame(newTree)
    play = newGame.setUp()
    # if user want to play
    if play == True:
        ready = newGame.getReady("restricted")
        # if user ready
        if ready == True:
            replay = newGame.restart()
            # if user want replay
            while replay == True:
                newGame.present()
                check = newGame.getReady("restricted")
                if check == False:
                    replay = False
                else:
                    replay = newGame.restart()

if __name__ == '__main__':
    main()
