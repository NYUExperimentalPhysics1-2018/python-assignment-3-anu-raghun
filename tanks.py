#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:18:02 2018

@author: gershow
@Author: Anu Raghunathan, ar4914
"""
import numpy as np
import matplotlib.pyplot as plt
import math

tank1Color = 'b'
tank2Color = 'r'
obstacleColor = 'k'

##### functions you need to implement #####
def trajectory (x0,y0,v,theta,g = 9.8, npts = 1000):
    v=float(v)
    y0=float(y0)
    x0=float(x0)
    theta=float((theta*math.pi)/180)
    
    vx_0=v*math.cos(theta)
    vy_0=v*math.sin(theta)
    
    t_final=(vy_0/g)+math.sqrt(((vy_0/g)**2)-(2*(y0/g)))
    times=np.linspace(0,t_final,npts)
    
    x_t=x0+vx_0*(times)
    y_t=y0+vy_0*(times)-(0.5*g)*(times)**2
    trajectory=(x_t,y_t)
    return trajectory

def firstInBox (x,y,box):
    val=-1
    for j,a in enumerate(x):
        if ((box[0]<=x[j]<=box[1])&(box[2]<=y[j]<=box[3])):
            val=j
    return val
            


def tankShot (targetBox, obstacleBox, x0, y0, v, theta, g = 9.8):
    x,y=trajectory(x0,y0,v,theta)
    if firstInBox(x,y,obstacleBox)>=0:
        hit=0
        x,y=endTrajectoryAtIntersection(x,y,obstacleBox)
    if firstInBox(x,y,targetBox)>=0:
        hit=1
    else:
        hit=0
    plt.plot(x,y)
    return hit



def drawBoard (tank1box, tank2box, obstacleBox, playerNum):
    plt.clf()
    drawBox(tank1box,'r')
    drawBox(tank2box,'b')
    drawBox(obstacleBox,'g')
    plt.xlim(0,100)
    plt.ylim(0,100)   
   
    showWindow() #this makes the figure window show up

def oneTurn (tank1box, tank2box, obstacleBox, playerNum, playerName, g = 9.8):   
    velocity=int(input(playerName+', what is your velocity value?  '))
    angle=int(input('At what angle?   '))
    drawBoard(tank1box,tank2box,obstacleBox,playerNum)

    
    if playerNum==1:
        origin=tank1box
        target=tank2box
    else:
        origin=tank2box
        target=tank1box
        
    x0=(0.5)*(origin[0]+origin[1])  
    y0=(0.5)*(origin[2]+origin[3])  
    result=tankShot(target,obstacleBox,x0,y0,velocity,angle)
    if result==1:
        return playerNum
    else:
        return 0

    

def playGame(tank1box, tank2box, player1Name, player2Name, obstacleBox, g = 9.8):
    playerNum=2
    while True:
        playerNum=3-playerNum
        if playerNum==1:
            hit=oneTurn(tank1box,tank2box,obstacleBox, playerNum, player1Name)
        else:
            hit=oneTurn(tank1box,tank2box,obstacleBox, playerNum, player2Name)
        if hit>0:
            break
        input("Press Enter to continue...")
    if playerNum==1:
        print('Congratulations '+player1Name+'!')
    else:
        print('Congratulations '+player2Name+'!')  

    
        
##### functions provided to you #####
def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list, optional
               two element list of form [min, max]
               value entered must be in range [min, max] inclusive
        Returns
        -------
            float
                number entered by user
    """
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
            
    return num    

def showWindow():
    """
    shows the window -- call at end of drawBoard and tankShot
    """
    plt.draw()
    plt.pause(0.001)
    plt.show()


def drawBox(box, color):
    """
    draws a filled box in the current axis
    parameters
    ----------
    box : tuple
        (left,right,bottom,top) - extents of the box
    color : str
        color to fill the box with, e.g. 'b'
    """    
    x = (box[0], box[0], box[1], box[1])
    y = (box[2], box[3], box[3], box[2])
    ax = plt.gca()
    ax.fill(x,y, c = color)

def endTrajectoryAtIntersection (x,y,box):
    """
    portion of trajectory prior to first intersection with box
    
    paramaters
    ----------
    x,y : np array type
        position to check
    box : tuple
        (left,right,bottom,top)
    
    returns
    ----------
    (x,y) : tuple of np.array of floats
        equal to inputs if (x,y) does not intersect box
        otherwise returns the initial portion of the trajectory
        up until the point of intersection with the box
    """
    i = firstInBox(x,y,box)
    if (i < 0):
        return (x,y)
    return (x[0:i],y[0:i])


##### fmain -- edit box locations for new games #####
def main():
    tank1box = [10,15,0,5]
    tank2box = [90,95,0,5]
    obstacleBox = [40,60,0,50]
    player1Name=input('What is player 1''s name?  ')
    player2Name=input('What is player 2''s name?  ')
    playGame(tank1box, tank2box, player1Name, player2Name, obstacleBox)
    

#don't edit the lines below;
if __name__== "__main__":
    main()  
        
    