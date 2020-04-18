# Peter Finnerty - Project 2020
# Write a program called analysis.py that:
# • outputs a summary of each variable to a single text file,
# • saves a histogram of each variable to png files, and
# • outputs a scatter plot of each pair of variables.
#-----------------------------------------------------------
import math

class Point3D():
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
        
        
p1 = Point3D(5.1, 3.4, 2.0)
print(p1.distance() )

p2 = Point3D(6.5, 7.6, 3.7)
print(p2.distance () )
