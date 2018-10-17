import random
import math
import matplotlib.pyplot as pyplot
import numpy as py

#================================= Random Walk Function ==========================

def drunkWalk(n):

    """
This function is the random Walk function similar to the previous code. The simulation is the
same as the previous inside a circular enclosure.
Parameters:
n = number of steps taken

Output:
x = number of steps to leave the enclosure

    """

    xcor = 0
    ycor = 0
    x = 0
    
    #simulating the drunk walk

    for i in range(n+1):

        x = x+1

        if x <= 1000:
            angle = random.uniform(0,360)
            dist = random.uniform(0,10)
            xcor = xcor + math.cos(angle)*dist
            ycor = ycor + math.sin(angle)*dist

            rad = math.sqrt(xcor**2 + ycor**2)
            
            angleP = math.degrees(math.atan(xcor/ycor))

            if (rad > 100) and (0 <= angleP <= 30):

                return x                #returning values for the xlist

        else:

            return x-1

#================================= Main Function including Hist ==========================


def main():

    #number of particles

    n = 1000 
    sim = 3000              #following pyplot plotted as a simulation of 3000 similar particles               #number of steps for each particle
    xlist = []
    for i in range(sim):

        x = drunkWalk(n)
        xlist.append(x)


#parameters for histogram using pyplot
    bins = py.arange(0, 1001, 100)                  #bin size = 100
    pyplot.hist(xlist, bins)
    pyplot.xlabel('Steps taken by particle')
    pyplot.ylabel('Successful escapes from the enclosure')
    pyplot.title('Analysis of Number of Steps Taken to Escape Enclosure')
    pyplot.show()

main()
