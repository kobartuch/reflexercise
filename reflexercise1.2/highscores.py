from __future__ import print_function, division
import os
import time
import traceback
import sys
from random import randint
from graphics import *

def class highScores:
    list_of_scores = []
    
   def add_to_highscores(self, x):
       return list_of_scores.append(x)

   def return_highscores(self):
       return list_of_scores

   def print_scores(self):
       for s in list_of_scores:
           print(s)
