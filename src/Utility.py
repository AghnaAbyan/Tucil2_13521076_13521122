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

# arrayOfPoint = createRandomPoint(3)
# print(arrayOfPoint)
# shortest, Point1, Point2, indeks1, indeks2 = BFSolution(arrayOfPoint)
# print(shortest)
# print(Point1)
# print(Point2)
# print(indeks1)
# print(indeks2)

