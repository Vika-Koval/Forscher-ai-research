# problem: https://cms.ucu.edu.ua/mod/vpl/view.php?id=356223&userid=9747
# my code:
class Point:
    """Class Point"""
    def __init__(self, a, b):
        self.x = a
        self.y = b
class Line:
    """Class Line"""
    def __init__(self, p1: Point, p2: Point):
        if p1.x == p2.x and p1.y == p2.y:
            raise ValueError("This is just a dot")
        m = (p2.y - p1.y) / (p2.x - p1.x) if p2.x != p1.x else None
        self.ax = m
        if m is not None:
            self.b = -m * p1.x + p1.y
        else:
            self.b = p1.x
    def intersect(self, other):
        """Finds the point of intersection between two lines"""
        if self.ax is None:
            if other.ax is None:
                if self.b == other.b:
                    return 1
                else:
                    return None
            x = self.b
            y = other.ax * x + other.b
            return Point(x, y)
        if other.ax is None:
            x = other.b
            y = self.ax * x + self.b
            return Point(x, y)
        if self.ax == other.ax:
            if self.b == other.b:
                return self.ax
            else:
                return None
        cx = self.ax - other.ax
        d = other.b - self.b
        if cx != 0:
            x = d / cx
            y = self.ax * x + self.b
            return Point(x, y)
        elif d != 0:
            return None
        else:
            return self.ax
# ------------------------------------------------------------------------------------
    # Request1: 
    # generate tests using module unittest in python for this task, i dont need you to write the code i only need unittests:
    # (the task info provided in cms translated in eng since it was giving nonsense when using ukr)
    # Blackbox's answer:
import unittest
class TestLine(unittest.TestCase):
    def setUp(self):
        from point import Point
        from line import Line
        self.p1 = Point(0.0, 0.0)
        self.p2 = Point(1.0, 3.0)
        self.p3 = Point(0.0, 0.0)
        self.p4 = Point(2.0, 2.0)
        self.line1 = Line(self.p1, self.p2)
        self.line2 = Line(self.p3, self.p4)
        self.line3 = Line(self.p1, self.p2)
    def test_no_intersection(self):
        # Test that the intersect method returns None when the lines do not intersect
        self.assertIsNone(self.line1.intersect(Line(Point(0.0, 1.0), Point(1.0, 4.0))))
    def test_intersection(self):
        # Test that the intersect method returns the correct point of intersection
        intersection = self.line1.intersect(self.line2)
        self.assertEqual(intersection.x, 0.5)
        self.assertEqual(intersection.y, 0.75)
    def test_matching_lines(self):
        # Test that the intersect method returns the first argument when the lines match
        self.assertEqual(self.line1.intersect(self.line3), self.line1)
    def test_vertical_line(self):
        # Test that the intersect method can handle vertical lines
        line4 = Line(Point(0.0, 0.0), Point(0.0, 1.0))
        self.assertIsNone(self.line1.intersect(line4))
    def test_coincident_lines(self):
        # Test that the intersect method returns None when the lines are coincident
        line5 = Line(Point(0.0, 0.0), Point(1.0, 0.0))
        self.assertIsNone(self.line1.intersect(line5))
    def test_parallel_lines(self):
        # Test that the intersect method returns None when the lines are parallel
        line6 = Line(Point(0.0, 1.0), Point(1.0, 4.0))
        self.assertIsNone(self.line1.intersect(line6))
if __name__ == '__main__':
    unittest.main()
  
# most tests didn't pass, and after taking a closer look the tests were not valid.
# -------------------------------------------------------------------------------------
  # Request2:
  # try generating the tests again since it seems you made mathematical mistakes in some
# it became even worse
# ---------------------------------------------------------------------------------------
  # Request3:
  # try looking at how you calculate the results since it seems you lack knowledge of how intersections should be calculated
# without success
# after trying a couple of more times i lost hope
#######################################################################################
# lets now test how good blackbox is at optimizing
# let's say our unittests look like this:
import unittest
from line import Line, Point
class TestLineIntersection(unittest.TestCase):
    def test_no_intersection_parallel_lines(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(0, 1), Point(1, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_no_intersection_perpendicular_lines(self):
        line1 = Line(Point(0, 0), Point(1, 0))
        line2 = Line(Point(0, 1), Point(1, 1))
        self.assertIsNone(line1.intersect(line2))
    def test_intersection_at_point(self):
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(0, 2), Point(2, 0))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)
    def test_identical_lines(self):
        line1 = Line(Point(0, 0), Point(2, 2))
        line2 = Line(Point(0, 0), Point(2, 2))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_vertical_and_horizontal_lines(self):
        line1 = Line(Point(0, 0), Point(0, 2))
        line2 = Line(Point(-1, 1), Point(1, 1))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 0)
        self.assertEqual(intersection.y, 1)
    def test_horizontal_lines_with_different_y(self):
        line1 = Line(Point(0, 1), Point(2, 1))
        line2 = Line(Point(0, 2), Point(2, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_vertical_lines_with_different_x(self):
        line1 = Line(Point(1, 0), Point(1, 2))
        line2 = Line(Point(2, 0), Point(2, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_coincident_lines(self):
        line1 = Line(Point(0, 0), Point(1, 1))
        line2 = Line(Point(0, 0), Point(1, 1))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_vertical_lines_coincident(self):
        line1 = Line(Point(1, 0), Point(1, 2))
        line2 = Line(Point(1, 0), Point(1, 2))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_horizontal_lines_coincident(self):
        line1 = Line(Point(0, 1), Point(2, 1))
        line2 = Line(Point(0, 1), Point(2, 1))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_vertical_lines_parallel(self):
        line1 = Line(Point(1, 0), Point(1, 2))
        line2 = Line(Point(2, 0), Point(2, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_horizontal_lines_parallel(self):
        line1 = Line(Point(0, 1), Point(2, 1))
        line2 = Line(Point(0, 2), Point(2, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_coincident_vertical_lines_different_y(self):
        line1 = Line(Point(1, 0), Point(1, 2))
        line2 = Line(Point(1, 1), Point(1, 3))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_coincident_horizontal_lines_different_x(self):
        line1 = Line(Point(0, 1), Point(2, 1))
        line2 = Line(Point(1, 1), Point(3, 1))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_negative_slope_lines_intersecting(self):
        line1 = Line(Point(1, 3), Point(3, 1))
        line2 = Line(Point(1, 1), Point(3, 3))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 2)
        self.assertEqual(intersection.y, 2)
    def test_lines_with_zero_slope_intersecting(self):
        line1 = Line(Point(1, 1), Point(3, 1))
        line2 = Line(Point(2, 2), Point(4, 2))
        self.assertIsNone(line1.intersect(line2))
    def test_vertical_lines_with_same_x_coordinate(self):
        line1 = Line(Point(1, 0), Point(1, 2))
        line2 = Line(Point(1, 1), Point(1, 3))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
    def test_horizontal_lines_with_same_y_coordinate(self):
        line1 = Line(Point(0, 1), Point(2, 1))
        line2 = Line(Point(1, 1), Point(3, 1))
        intersection = line1.intersect(line2)
        self.assertIsInstance(intersection, Line)
if __name__ == '__main__':
    unittest.main()
# ---------------------------------------------------------------------------------
    # Request1:
    # organize and optimize the tests. for instance, group the different functions into one if necessary and remove unnecessary tests for better speed. you can try using setup and teardown
    # (the tests)
    # Blackbox's response:
import unittest
from line import Line, Point
class TestLineIntersection(unittest.TestCase):
    def setUp(self):
        self.line1 = Line(Point(0, 0), Point(1, 1))
        self.line2 = Line(Point(0, 1), Point(1, 2))
    def test_no_intersection(self):
        # Test parallel lines
        self.assertIsNone(self.line1.intersect(self.line2))
        # Test perpendicular lines
        line3 = Line(Point(0, 0), Point(1, 0))
        line4 = Line(Point(0, 1), Point(1, 1))
        self.assertIsNone(line3.intersect(line4))
        # Test horizontal lines with different y
        line5 = Line(Point(0, 1), Point(2, 1))
        line6 = Line(Point(0, 2), Point(2, 2))
        self.assertIsNone(line5.intersect(line6))
        # Test vertical lines with different x
        line7 = Line(Point(1, 0), Point(1, 2))
        line8 = Line(Point(2, 0), Point(2, 2))
        self.assertIsNone(line7.intersect(line8))
    def test_intersection(self):
        # Test intersection at a point
        line3 = Line(Point(0, 0), Point(2, 2))
        line4 = Line(Point(0, 2), Point(2, 0))
        intersection = line3.intersect(line4)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 1)
        self.assertEqual(intersection.y, 1)
        # Test vertical and horizontal lines
        line5 = Line(Point(0, 0), Point(0, 2))
        line6 = Line(Point(-1, 1), Point(1, 1))
        intersection = line5.intersect(line6)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 0)
        self.assertEqual(intersection.y, 1)
    def test_identical_lines(self):
        # Test identical lines
        line3 = Line(Point(0, 0), Point(2, 2))
        line4 = Line(Point(0, 0), Point(2, 2))
        intersection = line3.intersect(line4)
        self.assertIsInstance(intersection, Line)
        # Test coincident lines
        line5 = Line(Point(0, 0), Point(1, 1))
        line6 = Line(Point(0, 0), Point(1, 1))
        intersection = line5.intersect(line6)
        self.assertIsInstance(intersection, Line)
        # Test vertical lines coincident
        line7 = Line(Point(1, 0), Point(1, 2))
        line8 = Line(Point(1, 0), Point(1, 2))
        intersection = line7.intersect(line8)
        self.assertIsInstance(intersection, Line)
        # Test horizontal lines coincident
        line9 = Line(Point(0, 1), Point(2, 1))
        line10 = Line(Point(0, 1), Point(2, 1))
        intersection = line9.intersect(line10)
        self.assertIsInstance(intersection, Line)
    def test_negative_slope_lines(self):
        # Test negative slope lines intersecting
        line3 = Line(Point(1, 3), Point(3, 1))
        line4 = Line(Point(1, 1), Point(3, 3))
        intersection = line3.intersect(line4)
        self.assertIsInstance(intersection, Point)
        self.assertEqual(intersection.x, 2)
        self.assertEqual(intersection.y, 2)
if __name__ == '__main__':
    unittest.main()
# time before: 0.003s, coverage: 80%
# time after: 0.001s, coverage: 73%
# blackbox improved the speed but the coverage decreased. also it removed too many tests to the point that almost all the tests passed on the old not fully working code
#####################################################################################################
# 
