import math #math and unittest library has pre-written math functions
import unittest

def circleArea(radius):
    """Returns the area of a circle"""
    return math.pi*radius*radius

def rectArea(base, height):
    """Returns the area of a rectangle"""
    return base*height

def trapArea(base1, base2, height):
    """Returns the area of a trapezoid"""
    return (base1+base2)/2*height

def triArea(base,height):
    """Returns the area of a triangle"""
    return 0.5*base*height
    
	
class MyTest(unittest.TestCase): 
    def testCircleArea(self):
        self.assertAlmostEqual(circleArea(5), math.pi*25)
    def testRectArea(self):
        self.assertAlmostEqual(rectArea(2,3), 6)
    def testTrapArea(self):
        self.assertAlmostEqual(trapArea(3,6,2), 9)
    def testTriArea(self):
        self.assertAlmostEqual(triArea(4,7), 14)
    
    