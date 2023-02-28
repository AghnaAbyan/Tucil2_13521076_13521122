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
            temp = random.uniform(-1e6,1e6)
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
    #Point1 dan Point2 adalah 2 poin dengan jarak terpendek
    Point1 = [] 
    Point2 = []
    count = 0 #banyak fungsi euclidianDistance dipanggil
    for i in range(0, len(arrayOfPoint) - 1):
        for j in range(i+1, len(arrayOfPoint)):
            distance = euclidianDistance(arrayOfPoint[i], arrayOfPoint[j])
            count += 1
            if(distance < shortest):
                shortest = distance
                Point1 = arrayOfPoint[i]
                Point2 = arrayOfPoint[j]

    return shortest, Point1, Point2, count

# def partitionOnX(arrayOfPoints, i, j):
#     pivot = arrayOfPoints[(i+j)//2][0]
#     p = i
#     q = j
#     while p < q:
#         while arrayOfPoints[p][0] < pivot:
#             p += 1
#         while arrayOfPoints[q][0] > pivot:
#             q -= 1
#         if p <= q:
#             if p != q:
#                 temp = arrayOfPoints[p]
#                 arrayOfPoints[p] = arrayOfPoints[q]
#                 arrayOfPoints[q] = temp
#             p += 1
#             q -= 1
#     return q

def quicksort(arrayOfPoints):
    if(len(arrayOfPoints) == 0):
        #jika list tidak memiliki elemen sama sekali maka tidak perlu disorting
        return []
    elif (len(arrayOfPoints) == 1):
        #jika list hanya memiliki satu elemen tidak perlu disorting
        return arrayOfPoints
    else:
        pivot = arrayOfPoints[len(arrayOfPoints) // 2][0] # Ambil elemen yang ada ditengah list sebagai pivot
        left = []
        equal = []
        right = []

        for point in arrayOfPoints:
            if (point[0] < pivot):
                #jika nilai x pada point lebih kecil dari pivot, maka point akan dimasukkan ke array left
                left.append(point)
            elif (point[0] == pivot):
                #jika nilai x pada point sama dengan pivot, maka point akan dimasukkan ke array equal
                equal.append(point)
            else:
                #jika nilai x pada point lebih besar dari pivot, maka point akan dimasukkan ke array besar
                right.append(point)

        
        return quicksort(left) + equal + quicksort(right) #rekursi

def visualize (arrayOfPoint, Point1, Point2):
    if(len(Point1) > 3):
        print("Gabisa divisualisaiin gan, kamu bukan dewa yang bisa liat 3 dimensi keatas !!!!!")
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        #X,Y,Z adalah list yang digunakan untuk menampung komponen x,y,z dari point
        X = []
        Y = []
        Z = []
        for point in (arrayOfPoint):
            if(point != Point2 and point != Point1):
                #jika point berbeda dari 2 point terdekat, maka nilai komponen x,y,z akan dimasukan kedalam list
                X.append(point[0])
                Y.append(point[1])
                Z.append(point[2])
        
        ax.scatter(X, Y, Z, color = "blue") #warnai biru untuk point yang bukan dua point terdekat

        #untuk 2 point terdekat akan diberi warna merah
        ax.scatter(Point1[0], Point1[1], Point1[2], color = "red")
        ax.scatter(Point2[0], Point2[1], Point2[2], color = "red")
        #memberi garis warna merah yang menghubungkan dua titik terdekat
        ax.plot([Point1[0], Point2[0]], [Point1[1], Point2[1]], [Point1[2], Point2[2]], color = "red")

        # Set the axis labels
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Show the plot
        plt.show()

def closestPairWithDnC (arrayOfPoint):
    if (len(arrayOfPoint) <= 3):
        #jika ukuran array kurang atau sama dengan 3, maka akan langsung diselesaikan menggunakan bruteforce
        return BFSolution(arrayOfPoint)
    else:
        mid = len(arrayOfPoint)//2
        #split array menjadi 2 bagian 
        left = arrayOfPoint[:mid]
        right = arrayOfPoint[mid:]
        middleX = (left[len(left)-1][0] + right[0][0])/2 #koordinat X yang membagi arrayOfPoints menjadi 2
        #divide
        distanceLeft , Point1L, Point2L, count1 = closestPairWithDnC(left)
        distanceRight, Point1R, Point2R, count2 = closestPairWithDnC(right)
        count = count1 + count2 #banyak operasi perhitungan
        closest = 0
        Point1 = []
        Point2 = []
        #conquer
        if(distanceLeft > distanceRight):
            closest = distanceRight
            Point1 = Point1R
            Point2 = Point2R
        else:
            closest = distanceLeft
            Point1 = Point1L
            Point2 = Point2L

        inMiddleRange = []
        for i in range(0, len(arrayOfPoint)):
            if(abs(arrayOfPoint[i][0]- middleX) < closest):
                #mencari titik titik yang berada di range middle - closest sampai middle + closest
                inMiddleRange.append(arrayOfPoint[i])
        for i in range (0, len(inMiddleRange)-1):
            for j in range(i+1, len(inMiddleRange)):
                if(abs(inMiddleRange[j][1] - inMiddleRange[i][1]) < closest): #jika jarak titik indeks ke j dan i pada sumbu y kurang dari closest, baru dilakukan perhitungan
                    distanceMid = euclidianDistance(inMiddleRange[j], inMiddleRange[i])
                    count +=1
                    if(distanceMid < closest):
                        closest = distanceMid
                        Point1 = inMiddleRange[i]
                        Point2 = inMiddleRange[j]
                
        return closest, Point1, Point2, count