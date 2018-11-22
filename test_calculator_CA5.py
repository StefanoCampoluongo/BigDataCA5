# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 15:34:21 2018

@author: campo
"""

import unittest
from functools import reduce

from calculator_CA5 import add, cosine, cube, division, exponent, multiply, sine, square, squareRoot, subtraction
class CalculatorTest(unittest.TestCase):
    
    def testAdd(self):
        #testing integers
        self.assertEqual(7,add([2,3,2]))
        ##negative numbers
        self.assertEqual(-11 ,add([-6,-3,-2]))
        #testing floats
        self.assertEqual(7.9 ,add([3.7,4.2]))
        self.assertEqual(11.9 ,add([3.7,4.2,1,3]))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex",add(["one","two",3]))
        #testing complex numbers
        self.assertEqual(5-8j,add([3-2j,2-6j]))

    def testCosine(self):
        #test cosine
        self.assertEqual([0,-1,0.932134327241114, 0.707106781186548,-1,0],cosine([90,180,21.23,45,-180,450]))
        ##testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int or float",cosine(["twenty",90]))

    def testCube(self):
        #testing cube
        self.assertEqual([64,0,-8,30.371328000000002,(-9+46j)],cube([4,0,-2,3.12,(3+2j)]))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex",cube([4,0,-2,'five']))
    
    def testDivision(self):
        #testing division
        self.assertEqual(1,division([4,2,2]))
        ##zeros
        self.assertEqual(0,division([0,5,3,2,3]))
        self.assertEqual("Division by zero not allowed",division([20,5,3,0,3]))     
        #testing floats and negatives
        self.assertEqual(0.8,division([3.2,2,2]))
        self.assertEqual(0.17,round(division([3.2,2.3,2,4]),2))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex", division([20,5,'four',3,0,3])) 
        #testing complex numbers
        self.assertEqual(-0.2+0.4j,division([1+2j,3-4j,1]))
        
    def testExponent(self):
        #testing integers
        self.assertEqual(32768,exponent([2,3,5]))
        ##1 by the power of x is 1
        self.assertEqual(1,exponent([1,3,2,3]))
        ##zeros
        self.assertEqual(0,exponent([0,5,8,2]))
        self.assertEqual("0 cannot be raised to a negative power",exponent([0,3,8,-5,2]))
        #testing floats and negatives
        self.assertEqual(0.125,exponent([2,-3]))
        #testing strings insertion
        self.assertEqual('Elements in the input list can only be int, float or complex',exponent([1,3,'two',3]))
        #testing complex numbers
        self.assertEqual(5+12j,exponent([3+2j,2]))
    
    def testMultiply(self):
        #testing integers
        self.assertEqual(30 ,multiply([5,3,2]))
        ##zeros
        self.assertEqual(0,multiply([5,0,3,2,2.2]))
        ##negative numbers and floats
        self.assertEqual(-7.5 ,multiply([5,-3,0.5]))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex",multiply([2,4,3.2,"two"]))
        #testing complex numbers
        self.assertEqual(35-6j ,multiply([3-2j,9+4j]))
         
    def testSine(self):
        #test sine
        self.assertEqual([1,0.707106781186548,0,0,-1,0.362112684089851,1],sine([90,45,0,180,-90,21.23,450]))
        ##testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int or float",sine(["twenty",90]))
       
    def testSquare(self):
        #testing square
        self.assertEqual([16,0,4,9.7344,(5+12j)],square([4,0,-2,3.12,3+2j]))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex",square([4,0,-2,'five']))

    def testSquareRoot(self):
        #testing square root
        self.assertEqual([2, 0, 1.5231546211727816],squareRoot([4,0,2.32]))
        #testing the insertion of strings
        self.assertEqual("Each element in the input list must be a positive number",squareRoot([4,0,'two',2.32]))
           
    def testSubtraction(self):
        #testing integers
        self.assertEqual(3 ,subtraction([9,4,2]))
        ##negative numbers
        self.assertEqual(10 ,subtraction([5,-3,-2]))
        #testing floats
        self.assertEqual(-1.5 ,subtraction([3.7,4.2,1]))
        #testing the insertion of strings
        self.assertEqual("Elements in the input list can only be int, float or complex" ,subtraction([5,-3,-2, 'four']))
        #testing complex numbers
        self.assertEqual(1+4j ,subtraction([3-2j,2-6j]))
               
if __name__ == '__main__':
    unittest.main()