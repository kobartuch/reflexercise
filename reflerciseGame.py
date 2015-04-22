from __future__ import print_function, division
import os
import time
import traceback
import sys
from random import randint
from graphics import *

class reflexerciseGame:
    def __init__(self):
        self.gui_Window()
        
    #def timer():

    def gui_Window(self):
        win = GraphWin("Reflexercise", 1024, 780)
        win.setBackground("grey")

    #check if mouseclick is inside target
       # if win.getMouse() ==
            #Undraw target and show timer
            #USE THIS FOR TIMER: http://stackoverflow.com/questions/22610043/how-do-i-create-a-reaction-timer-in-python-as-gui

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
            print(timerEnd - timerStart)
                    
            
if __name__=='__main__':
    reflexer = reflexerciseGame()
    reflexer.main()
