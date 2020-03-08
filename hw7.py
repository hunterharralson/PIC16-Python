#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hunter Harralson
304-781-158
PIC 16

Homework 7: Knights Tour 
"""

import tkinter as tk
import math


class Knights_tour(tk.Frame):
    def __init__(self, parent, board_size):
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent
        self.board = tk.Canvas(self, width = 500, height = 500)
        self.board.pack()
        self.inc = round(500/int(board_size)) # increment 
        
        # create lines on the chess board
        self.board_size = int(board_size)
        self.board.bind('<Configure>', self.create_grid)
        
        # starting piece 
        self.board.create_rectangle(0,0,self.inc,self.inc,fill="orange")
        self.board.pack()
        
        # quit button
        self.quit_button = tk.Button(
                self, 
                text = 'Quit Game', 
                command = self.terminate,
                height = 5,
                width = 20)
        self.quit_button.pack()
        
        self.position = [0,0] # x1, y1
        
        self.board.bind("<Button-1>", lambda event, arg=self.position: self.button_press(event, self.position))
    
    # Ends the game
    def terminate(self):
        self.quit_button.configure(text="GAME OVER")
        self.quit()
        
    # Fills in a square in valid positions 
    def button_press(self, event, position):
        w = self.board.winfo_width() # Get current width of canvas
        inc = round(w/self.board_size) # inc = increment
        
        # create a square range for fill 
        x1 = math.floor(event.x/inc)*inc
        x2 = math.ceil(event.x/inc)*inc
        y1 = math.floor(event.y/inc)*inc
        y2 = math.ceil(event.y/inc)*inc
        
        # Valid Move 1: x +- 1, y +- 2
        if ((x1 == self.position[0]+inc or x1 == self.position[0]-inc) and
            (y1 == self.position[1]-(2*inc) or y1 == self.position[1]+(2*inc))):
            self.board.create_rectangle(x1, y1,
                                        x2, y2,
                                        fill="orange") # makes new square orange
            self.board.create_rectangle(self.position[0],self.position[1],
                                       self.position[0]+inc,self.position[1]+inc,
                                       fill="blue") # makes old square blue
            self.position = [x1,y1] # update current position
            
        # Valid Move 2: x +- 2, y +- 1
        elif ((x1 == self.position[0]+(2*inc) or x1 == self.position[0]-(2*inc)) and 
              (y1 == self.position[1]-inc or y1 == self.position[1]+inc)):
            self.board.create_rectangle(x1, y1,
                                        x2, y2,
                                        fill="orange")
            self.board.create_rectangle(self.position[0],self.position[1],
                                       self.position[0]+inc,self.position[1]+inc,
                                       fill="blue")
            self.position = [x1,y1]
            
        else:
            pass
    
    def create_grid(self, event=None): 
        w = self.board.winfo_width() # Get current width of canvas
        h = self.board.winfo_height() # Get current height of canvas
        increment = w/self.board_size # how spaced each line is
        
        self.board.delete('grid_line') # Will only remove the grid_line

        # Creates all vertical lines at intevals of 100
        for i in range(0, w, round(increment)):
            self.board.create_line([(i, 0), (i, h)], tag='grid_line')

        # Creates all horizontal lines at intevals of 100
        for i in range(0, h, round(increment)):
            self.board.create_line([(0, i), (w, i)], tag='grid_line')
    
    
def knights_tour(board_size): 
    #board_size = input("How many squares per row/column (5-10)?\n")
    root = tk.Tk()
    app = Knights_tour(root, board_size) 
    root.mainloop()
    

if __name__ == '__main__':
    board_size = input("How many squares per row/column (5-10)?\n")
    knights_tour(board_size)