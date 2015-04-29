from __future__ import print_function, division
import os
import time
import traceback
import sys
from random import randint
from graphics import *

## Find a python to .exe program which works for python 3.4 and use to
## create working executable for final game

##v1.2##
class reflexerciseGame:
    '''def __init__(self):
        self.gui_Window()'''

    '''Creates background window of GUI'''
    def gui_Window(self):
        win = GraphWin("Reflexercise", 1024, 780)
        win.setBackground("grey")

        '''
        highscoresTab = Rectangle(Point(300,200), Point(400,200))
        highscoresTab.setOutline("black")
        highscoresTab.draw(win)'''

    #check if mouseclick is inside target
       # if win.getMouse() ==
            #Undraw target and show timer
            #USE THIS FOR TIMER: http://stackoverflow.com/questions/22610043/how-do-i-create-a-reaction-timer-in-python-as-gui

    '''Draws the targets on the user's screen'''
    def draw_target():
        target = Circle(Point(512, 340), 30)
        target2 = Circle(Point(512, 340), 50)
        target3 = Circle(Point(512, 340), 70)

        target.setOutline("red")
        target2.setOutline("yellow")
        target3.setOutline("red")
    
        target.draw(win)
        target2.draw(win)
        target3.draw(win)
        
    def main(self):
        started = False
        clickedTarget = False
        randomInt = randint(0,9)
        self.gui_Window()
        
        while started == True:
            if randomInt >= 6:
                self.draw_target()
                timerStart = time.clock()

                if win.getMouse() == target.getRadius():
                    timerEnd = time.clock()
                    clickedTarget = True
                    started = False
            timeCounted = timerEnd - timerStart
            print(timeCounted)
                    
            
if __name__=='__main__':
    reflexer = reflexerciseGame()
    reflexer.main()
