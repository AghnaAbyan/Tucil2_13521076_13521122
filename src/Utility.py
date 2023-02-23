import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

#point = array dengan ukuran dimensi (default 3 dimensi)
#array of point array yang berisi point point
def createRandomPoint (n, dimensy = 3):
    arrayOfPoint = []
    for i in range(n):
        Point = []
        for j in range(dimensy):
            temp = random.uniform(0,100)
            Point.append(temp)
        arrayOfPoint.append(Point)
    return arrayOfPoint

def euclidianDistance (Point1, Point2):
    disctance = 0
    for i in range(len(Point1)):
        disctance += (Point2[i] - Point1[i])**2
    disctance = disctance**(1/2)
    return disctance

def BFSolution (arrayOfPoint):
    shortest = 9999999999999
    Point1 = []
    Point2 = []
    indeks1 = 0
    indeks2 = 0
    for i in range(0, len(arrayOfPoint)-1):
        for j in range(i+1, len(arrayOfPoint)):
            distance = euclidianDistance(arrayOfPoint[i], arrayOfPoint[j])
            if(distance < shortest):
                shortest = distance
                Point1 = arrayOfPoint[i]
                Point2 = arrayOfPoint[j]
                indeks1 = i
                indeks2 = j

    return shortest, Point1, Point2, indeks1, indeks2

def visualize (arrayOfPoint, Point1, Point2):
    if(len(Point1) > 3):
        print("Gabisa divisualisaiin mas, kamu bukan dewa yang bisa liat 3 dimensi keatas !!!!!")
    else:
        arrayOfPoint = np.array(arrayOfPoint)
        # Create a 3D plot
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot the data as points
        ax.scatter(arrayOfPoint[:,0], arrayOfPoint[:,1], arrayOfPoint[:,2])

        ax.plot(Point1[0], Point1[1], Point1[2], color = "black")
        ax.plot([Point1[0], Point2[0]], [Point1[1], Point2[1]], [Point1[2], Point2[2]], color = "black")

        # Set the axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Show the plot
        plt.show()

arrayOfPoint = createRandomPoint(64,3)
data = np.array(arrayOfPoint)
print(arrayOfPoint)
shortest, Point1, Point2, indeks1, indeks2 = BFSolution(arrayOfPoint)
print(shortest)
print(Point1)
print(Point2)
print(indeks1)
print(indeks2)

show = input("Mau divisualisasiin gak gan? (Y/N)")
if(show == "Y"):
    visualize(arrayOfPoint, Point1, Point2)


