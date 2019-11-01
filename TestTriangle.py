import unittest

from Triangle import classify_triangle

class TestTriangles(unittest.TestCase):


    def testInvalidTriangles(self):
        self.assertEqual(classify_triangle(1,3,5),'1,3,5 is not a Triangle')
    def testInvalidTriangles2(self):
        self.assertEqual(classify_triangle(1,0,0),'1,0,0 is not a Triangle')
    def testInvalidTriangles3(self):
        self.assertEqual(classify_triangle(1,0,1),'1,0,1 is not a Triangle')

    def testRightTriangles(self):
        self.assertEqual(classify_triangle(3,4,5),'3,4,5 is a Right triangle')
    def testRightTriangles2(self):
        self.assertEqual(classify_triangle(5,3,4),'5,3,4 is a Right triangle')
    def testRightTriangles3(self):
        self.assertEqual(classify_triangle(4,5,3),'4,5,3 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classify_triangle(0,0,0),'0,0,0 is a  equilateral')
    def testEquilateralTriangles2(self):
        self.assertEqual(classify_triangle(-1,-1,-1),'-1,-1,-1 is a  equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classify_triangle(2,2,1),'2,2,1 is a  isoceles')
    def testIsocelesTriangles2(self):
        self.assertEqual(classify_triangle(2,1,2),'2,1,2 is a  isoceles')
    def testIsocelesTriangles3(self):
        self.assertEqual(classify_triangle(1,2,2),'1,2,2 is a  isoceles')

    def testScaleneTriangles(self):
        self.assertEqual(classify_triangle(1,3,5),'Scalene','1,3,5 is a  scalene')
    def testScaleneTriangles2(self):
        self.assertEqual(classify_triangle(5,7,9),'Scalene','5,7,9 is a scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()