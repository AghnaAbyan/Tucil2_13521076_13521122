import Utility as util
import time
from colorama import Fore, Back, Style

print(Fore.RED + "███████╗███████╗██╗      █████╗ ███╗   ███╗ █████╗ ████████╗    ██████╗  █████╗ ████████╗ █████╗ ███╗   ██╗ ██████╗ ")
print(Fore.YELLOW + "██╔════╝██╔════╝██║     ██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║██╔════╝ ")
print(Fore.YELLOW + "███████╗█████╗  ██║     ███████║██╔████╔██║███████║   ██║       ██║  ██║███████║   ██║   ███████║██╔██╗ ██║██║  ███╗")
print(Fore.GREEN + "╚════██║██╔══╝  ██║     ██╔══██║██║╚██╔╝██║██╔══██║   ██║       ██║  ██║██╔══██║   ██║   ██╔══██║██║╚██╗██║██║   ██║")
print(Fore.BLUE + "███████║███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║   ██║       ██████╔╝██║  ██║   ██║   ██║  ██║██║ ╚████║╚██████╔╝")
print(Fore.BLUE + "╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
print(Style.RESET_ALL)
                                                                                                                    
dimension = int(input("Mau berapa dimensi gan? "))
nPoint = int(input("Mau berapa titik gan? "))

arrayOfPoints = util.createRandomPoint(nPoint, dimension)
arrayOfPoints = util.quicksort(arrayOfPoints)
startBF = time.time()
shortest, Point1, Point2, count1 = util.BFSolution(arrayOfPoints)
endBF = time.time()

BFtime = endBF - startBF


startDnC = time.time()
shortestdnc, Point1dnc, Point2dnc, count2= util.closestPairWithDnC(arrayOfPoints)
endDnC = time.time()
DnCtime = endDnC - startDnC

print(Fore.CYAN)
print("======================================Brute Force Solution======================================")
print("Jarak Terdekat                       : " +str(shortest))
print("Koordinat titik pertama              : " +str(Point1))
print("Koordinat titik kedua                : " +str(Point2))
print("Banyak operasi euclidian distance    : " +str(count1) + " total operasi ")
print("Waktu eksekusi                       : " +str(BFtime) + " detik (spek = Intel Core i7)")

print(Fore.MAGENTA)
print("======================================Divide and Conquer Solution======================================")
print("Jarak Terdekat                       : " +str(shortestdnc))
print("Koordinat titik pertama              : " +str(Point1dnc))
print("Koordinat titik kedua                : " +str(Point2dnc))
print("Banyak operasi euclidian distance    : " +str(count2) + " total operasi ")
print("Waktu eksekusi                       : " +str(DnCtime) + " detik (spek = Intel Core i7)")

print(Style.RESET_ALL)
visualise = input("Ketik (Y/y) jika titik ingin divisualisasikan, ketik tombol lainnya jika tidak!!! ")

if(visualise == "Y" or visualise == "y"):
    util.visualize(arrayOfPoints, Point1dnc, Point2dnc)
    print("Bye!!")
else:
    print("Bye!!")