from __future__ import print_function, division
import os
import time
import traceback
import sys
from graphics import *

def gui_Window():
    win = GraphWin("Reflexercise", 1024,780)
    win.setBackground("grey")
    
    target = Circle(Point(512, 340), 30)
    target2 = Circle(Point(512, 340), 50)
    target3 = Circle(Point(512, 340), 70)

    target.setOutline("red")
    target2.setOutline("yellow")
    target3.setOutline("red")
    
    target.draw(win)
    target2.draw(win)
    target3.draw(win)

    win.getMouse()
    win.close()



#def reflex_target():
    #target = Circle(Point(512, 340), 30)
    #target2 = Circle(Point(512, 340), 50)
    #target3 = Circle(Point(512, 340), 70)

#def draw_GUI():
gui_Window()


#def  
