'''
Created on Jan 16, 2016

@author: grovesr
'''
import unittest
from foo_bar.carrotland import answer as answer4_1
from foo_bar.carrotland import (IntegerPoint, IntegerSegment, IntegerTriangle,
                                IntegerOrthoRightTriangle,
                                IntegerOrthoRectangle) 

from math import sqrt
class TestAnswer(unittest.TestCase):
    
    def test1(self):
        vertices = [[-1000000000,-1000000000], [1000000000, 1000000000], [100, -100]]
        res = answer4_1(vertices)
        self.assertEqual(res, 198999999901)
    
    def test2(self):
        vertices = [[2, 3], [11, 7], [14, 19]]
        res = answer4_1(vertices)
        self.assertEqual(res,45)
    
    def test3(self):
        vertices = [[2, 3], [6, 9], [10, 160]]
        res = answer4_1(vertices)
        self.assertEqual(res, 289)
    
    def test4(self):
        vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
        res = answer4_1(vertices)
        self.assertEqual(res, 1730960165)
    
    def test5(self):
        vertices = [[0, 2], [4, 7], [10, 0]]
        res = answer4_1(vertices)
        self.assertEqual(res, 28)

class TestIntegerPointMethods(unittest.TestCase):
    
    def test_default_initialization(self):
        p1 = IntegerPoint()
        self.assertTupleEqual(p1.tuple(), (0, 0))
        
    def test_repr(self):
        p1 = IntegerPoint()
        self.assertEqual(repr(p1), '(0, 0)')
        
    def test_sub_p1_greater(self):
        p1 = IntegerPoint(1, 1)
        p2 = IntegerPoint(0, 1)
        res = p1 - p2
        self.assertTupleEqual(res.tuple(), (1, 0))
        
    def test_sub_p1_lesser(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        res = p1 - p2
        self.assertTupleEqual(res.tuple(), (-1, 0))
        
    def test_add(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        res = p1 + p2
        self.assertTupleEqual(res.tuple(), (1, 2))
        
    def test_equal(self):
        p1 = IntegerPoint(1, 1)
        p2 = IntegerPoint(1, 1)
        self.assertTrue(p1 == p2)

    def test_not_equal(self):
        p1 = IntegerPoint(1, 0)
        p2 = IntegerPoint(1, 1)
        self.assertFalse(p1 == p2)
    
    def test_touches_edge_ortho(self):
        p1 = IntegerPoint(1, 0)
        edge = IntegerSegment((0, 0), (2, 0))
        self.assertTrue(p1.touches_edge(edge))
    
    def test_touches_edge_non_ortho(self):
        p1 = IntegerPoint(1, 2)
        edge = IntegerSegment((0, 0), (2, 4))
        self.assertTrue(p1.touches_edge(edge))
    
    def test_doesnt_touch_edge_ortho(self):
        p1 = IntegerPoint(1, 1)
        edge = IntegerSegment((0, 0), (2, 0))
        self.assertFalse(p1.touches_edge(edge))
    
    def test_doesnt_touch_edge_non_ortho(self):
        p1 = IntegerPoint(1, 1)
        edge = IntegerSegment((0, 0), (2, 4))
        self.assertFalse(p1.touches_edge(edge))
        
class TestIntegerSegmentMethods(unittest.TestCase):
    
    def test_default_initialization(self):
        s1 = IntegerSegment()
        self.assertTupleEqual(s1.tuple(), ((0, 0), (0, 0)))
        
    def test_creation_from_tuple(self):
        s1 = IntegerSegment((0, 0), (2, 0))
        self.assertTupleEqual(s1.tuple(), ((0, 0), (2, 0)))
        
    def test_repr(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(0, 1))
        self.assertEqual(repr(s1), '(0, 0)->(0, 1)')
        
    def test_slope_inf(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(0, 1))
        self.assertEqual(s1.slope(), float('inf'))
        
    def test_slope_zero(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(1, 0))
        self.assertEqual(s1.slope(), 0)
    
    def test_slope_positive(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(2, 1))
        self.assertEqual(s1.slope(), 0.5)
        
    def test_slope_negative(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(2, -1))
        self.assertEqual(s1.slope(), -0.5)
        
    def test_length(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(3, 2))
        self.assertEqual(s1.length(), sqrt(3**2 + 2**2))
        
    def test_ortho_horiz(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(3, 0))
        self.assertTrue(s1.ortho())
        
    def test_ortho_vertical(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(0, 3))
        self.assertTrue(s1.ortho())
        
    def test_not_ortho(self):
        s1 = IntegerSegment(IntegerPoint(0, 0), IntegerPoint(3, 2))
        self.assertFalse(s1.ortho())
        
    def test_points(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        res = IntegerSegment(p1, p2)
        self.assertTupleEqual(res.vertices(), (p1, p2))
        
    def test_tuple(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        res = IntegerSegment(p1, p2)
        self.assertTupleEqual(res.tuple(), (p1.tuple(), p2.tuple()))
        
    def test_like_same_points(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        s1 = IntegerSegment(p1, p2)
        p3 = IntegerPoint(0, 1)
        p4 = IntegerPoint(1, 1)
        s2 = IntegerSegment(p3, p4)
        self.assertTrue(s1.like(s2))
        self.assertTrue(s2.like(s1))
        
    def test_like_reversed_points(self):
        p1 = IntegerPoint(0, 1)
        p2 = IntegerPoint(1, 1)
        s1 = IntegerSegment(p1, p2)
        p3 = IntegerPoint(0, 1)
        p4 = IntegerPoint(1, 1)
        s2 = IntegerSegment(p4, p3)
        self.assertTrue(s1.like(s2))
        self.assertTrue(s2.like(s1))
        
    def test_containing_pt_ct_zero_length(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(0, 0))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 1)
        
    def test_containing_pt_ct_horizontal(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(2, 0))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_containing_pt_ct_vertical(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(0, 2))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_containing_pt_ct_positive_unity_slope(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(2, 2))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_containing_pt_ct_negative_unity_slope(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(2, -2))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_containing_pt_ct_positive_non_unity_slope(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(4, 6))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_containing_pt_ct_negative_nonunity_slope(self):
        s1 = IntegerSegment(IntegerPoint(0,0), IntegerPoint(4, -6))
        res = s1.containing_pt_ct()
        self.assertEqual(res, 3)
        
    def test_doesnt_intersect_triangle_common_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(1, 2)
        t1 = IntegerTriangle(p1, p2, p3)
        s1 = IntegerSegment((2, 0), (2, 2))
        self.assertFalse(s1.intersects_triangle(t1))
        
    def test_doesnt_intersect_triangle_common_side(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(1, 2)
        t1 = IntegerTriangle(p1, p2, p3)
        s1 = IntegerSegment((-2, -1), (4, 2))
        self.assertFalse(s1.intersects_triangle(t1))
        
    def test_intersects_triangle(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(1, 2)
        t1 = IntegerTriangle(p1, p2, p3)
        s1 = IntegerSegment((0, 1), (3, 1))
        self.assertTrue(s1.intersects_triangle(t1))
        
class TestIntegerTriangleMethods(unittest.TestCase):
    
    def test_default_initialization(self):
        t1 = IntegerTriangle()
        self.assertTrue(t1._p1.tuple() == (0, 0) and 
                        t1._p2.tuple() == (0, 0) and
                        t1._p3.tuple() == (0, 0))
        
    def test_creation_from_tuple(self):
        t1 = IntegerTriangle((0, 0), (2, 0), (2,1))
        self.assertTupleEqual(t1.vertex_tuple(), ((0, 0), (2, 0), (2,1)))
    
    def test_repr(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(repr(t1), '(0, 0)->(2, 0)->(2, 1)')
        
    def test_vertices(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertTupleEqual(t1.vertices(), (p1, p2, p3)) 
        
    def test_sides(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        a = IntegerSegment(p1, p2)
        b = IntegerSegment(p2, p3)
        c = IntegerSegment(p3, p1)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertTupleEqual(t1.sides(), (a, b, c))

    
    def test_vertex_tuple(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertTupleEqual(t1.side_tuple(), (((0, 0), (2, 0)), 
                                                ((2, 0), (2, 1)), 
                                                ((2, 1), (0, 0))))
        
    def test_side_tuple(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertTupleEqual(t1.vertex_tuple(), ((0, 0), (2, 0), (2, 1)))
        
    def test_interior_edges_tuple_non_ortho(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(1, 2)
        t1 = IntegerTriangle(p1, p2, p3)
        interiorEdges = []
        for edgeTuple in t1.interior_edges_tuple():
            interiorEdges.append(IntegerSegment(edgeTuple))
        
        
        
    def test_circumscribed_rectangle_non_ortho_1_pt_common(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(1, 2)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, 0)
        rp3 = IntegerPoint(2, 2)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        self.assertTupleEqual(t1.circumscribed_rectangle().sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(t1.circumscribed_rectangle().vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_pos_slope_below_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(3, 1)
        p3 = IntegerPoint(5, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, 0)
        rp3 = IntegerPoint(5, 5)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        self.assertTupleEqual(t1.circumscribed_rectangle().sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(t1.circumscribed_rectangle().vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_pos_slope_above_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(1, 3)
        p3 = IntegerPoint(5, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, 0)
        rp3 = IntegerPoint(5, 5)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        self.assertTupleEqual(t1.circumscribed_rectangle().sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(t1.circumscribed_rectangle().vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_pos_slope_on_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 2)
        p3 = IntegerPoint(5, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, 0)
        rp3 = IntegerPoint(5, 5)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        self.assertTupleEqual(t1.circumscribed_rectangle().sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(t1.circumscribed_rectangle().vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_neg_slope_below_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(1, -3)
        p3 = IntegerPoint(5, -5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, -5)
        rp3 = IntegerPoint(5, 0)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        rect = t1.circumscribed_rectangle()
        self.assertTupleEqual(rect.sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(rect.vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_neg_slope_above_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(3, -1)
        p3 = IntegerPoint(5, -5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, -5)
        rp3 = IntegerPoint(5, 0)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        rect = t1.circumscribed_rectangle()
        self.assertTupleEqual(rect.sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(rect.vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
        
    def test_circumscribed_rectangle_non_ortho_2_pts_common_neg_slope_on_diagonal(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, -2)
        p3 = IntegerPoint(5, -5)
        t1 = IntegerTriangle(p1, p2, p3)
        rp1 = IntegerPoint(0, -5)
        rp3 = IntegerPoint(5, 0)
        a = IntegerSegment(rp1, IntegerPoint(rp3._x, rp1._y))
        b = IntegerSegment(IntegerPoint(rp3._x, rp1._y), rp3)
        c = IntegerSegment(rp3, IntegerPoint(rp1._x, rp3._y))
        d = IntegerSegment(IntegerPoint(rp1._x, rp3._y), rp1)
        rect = t1.circumscribed_rectangle()
        self.assertTupleEqual(rect.sides(), 
                              (a, b, c, d))
        self.assertTupleEqual(rect.vertices(), 
                              (a._p1, b._p1, c._p1, d._p1))
    
    def test_squaring_shapes_no_interior_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(5, 2)
        p3 = IntegerPoint(2, 5)
        p4 = IntegerPoint(5, 0)
        p5 = IntegerPoint(5, 5)
        p6 = IntegerPoint(0, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        expectedTriangle3 = IntegerTriangle(p1, p3, p6)
        self.assertEqual(len(shapes), 3)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle3)]), 1)
    
    def test_squaring_shapes_lower_right_interior_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(4, 2)
        p3 = IntegerPoint(6, 5)
        p4 = IntegerPoint(4, 0)
        p5 = IntegerPoint(6, 2)
        p6 = IntegerPoint(0, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        expectedTriangle3 = IntegerTriangle(p1, p3, p6)
        expectedRectangle = IntegerOrthoRectangle(p4, p5)
        self.assertEqual(len(shapes), 4)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle3)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedRectangle)]), 1)
        
    def test_squaring_shapes_upper_left_interior_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 4)
        p3 = IntegerPoint(6, 5)
        p4 = IntegerPoint(0, 4)
        p5 = IntegerPoint(2, 5)
        p6 = IntegerPoint(6, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        expectedTriangle3 = IntegerTriangle(p1, p3, p6)
        expectedRectangle = IntegerOrthoRectangle(p4, p5)
        self.assertEqual(len(shapes), 4)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle3)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedRectangle)]), 1)
        
    def test_squaring_shapes_lower_left_interior_vertex(self):
        p1 = IntegerPoint(0, 5)
        p2 = IntegerPoint(2, 1)
        p3 = IntegerPoint(6, 0)
        p4 = IntegerPoint(0, 1)
        p5 = IntegerPoint(2, 0)
        p6 = IntegerPoint(6, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        expectedTriangle3 = IntegerTriangle(p1, p3, p6)
        expectedRectangle = IntegerOrthoRectangle(p4, p5)
        self.assertEqual(len(shapes), 4)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle3)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedRectangle)]), 1)

    def test_squaring_shapes_upper_right_interior_vertex(self):
        p1 = IntegerPoint(0, 5)
        p2 = IntegerPoint(4, 4)
        p3 = IntegerPoint(6, 0)
        p4 = IntegerPoint(6, 4)
        p5 = IntegerPoint(4, 5)
        p6 = IntegerPoint(0, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p5)
        expectedTriangle2 = IntegerTriangle(p2, p3, p4)
        expectedTriangle3 = IntegerTriangle(p1, p3, p6)
        expectedRectangle = IntegerOrthoRectangle(p4, p5)
        self.assertEqual(len(shapes), 4)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle3)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedRectangle)]), 1)
        
    def test_interior_pt_ct_no_interior_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(5, 2)
        p3 = IntegerPoint(2, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 9)
        
    def test_interior_pt_ct_lower_right_interior_vertex(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(3, 1)
        p3 = IntegerPoint(4, 5)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 5)
        
    def test_common_edge_squaring_shapes_bottom(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 4)
        p3 = IntegerPoint(5, 0)
        p4 = IntegerPoint(0, 4)
        p5 = IntegerPoint(5, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        self.assertEqual(len(shapes), 2)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
    
    def test_common_edge_squaring_shapes_left(self):
        p1 = IntegerPoint(0, 4)
        p2 = IntegerPoint(5, 2)
        p3 = IntegerPoint(0, 0)
        p4 = IntegerPoint(5, 4)
        p5 = IntegerPoint(5, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        self.assertEqual(len(shapes), 2)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
    
    def test_common_edge_squaring_shapes_top(self):
        p1 = IntegerPoint(5, 4)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(0, 4)
        p4 = IntegerPoint(5, 0)
        p5 = IntegerPoint(0, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        self.assertEqual(len(shapes), 2)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
    
    def test_common_edge_squaring_shapes_right(self):
        p1 = IntegerPoint(5, 0)
        p2 = IntegerPoint(0, 2)
        p3 = IntegerPoint(5, 4)
        p4 = IntegerPoint(0, 0)
        p5 = IntegerPoint(0, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        expectedTriangle1 = IntegerTriangle(p1, p2, p4)
        expectedTriangle2 = IntegerTriangle(p2, p3, p5)
        self.assertEqual(len(shapes), 2)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle1)]), 1)
        self.assertTrue(len([shape for shape in shapes if shape.like(expectedTriangle2)]), 1)
    
    def test_common_edge_interior_pt_ct_bottom(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 4)
        p3 = IntegerPoint(5, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
    
    def test_common_edge_interior_pt_ct_left(self):
        p1 = IntegerPoint(0, 4)
        p2 = IntegerPoint(5, 2)
        p3 = IntegerPoint(0, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 8)
    
    def test_common_edge_interior_pt_ct_top(self):
        p1 = IntegerPoint(5, 4)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(0, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
    
    def test_common_edge_interior_pt_ct_right(self):
        p1 = IntegerPoint(5, 0)
        p2 = IntegerPoint(0, 2)
        p3 = IntegerPoint(5, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 8)
        
    def test_ortho_right_squaring_shapes(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(6, 0)
        p3 = IntegerPoint(6, 4)
        p4 = IntegerPoint(0, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        shapes = t1.squaring_shapes()
        self.assertEqual(len(shapes), 1)
        expectedTriangle = IntegerOrthoRightTriangle(p1, p3, p4)
        self.assertTrue(shapes[0].like(expectedTriangle))
        
    def test_ortho_right_interior_pt_ct_lower_right(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(6, 0)
        p3 = IntegerPoint(6, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
        
    def test_ortho_right_interior_pt_ct_upper_right(self):
        p1 = IntegerPoint(0, 4)
        p2 = IntegerPoint(6, 4)
        p3 = IntegerPoint(6, 0)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
        
    def test_ortho_right_interior_pt_ct_lower_left(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(6, 0)
        p3 = IntegerPoint(0, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
        
    def test_ortho_right_interior_pt_ct_upper_left(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(0, 4)
        p3 = IntegerPoint(6, 4)
        t1 = IntegerTriangle(p1, p2, p3)
        self.assertEqual(t1.interior_pt_ct(), 7)
            
from foo_bar.carrotland import IntegerOrthoRightTriangleInvalidError
class TestIntegerOrthoRightTriangleMethods(unittest.TestCase):
    
    def test_init_ortho_right(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 1)
        t1 = IntegerOrthoRightTriangle(p1, p2, p3)
        self.assertTrue(t1._p1.tuple() == (0, 0) and 
                        t1._p2.tuple() == (2, 0) and
                        t1._p3.tuple() == (2, 1))
        
    def test_init_non_ortho_right(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(1, 2)
        with self.assertRaises(IntegerOrthoRightTriangleInvalidError):
            IntegerOrthoRightTriangle(p1, p2, p3)
    
    def test_containing_pt_ct_points_on_hypotenuse(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(6, 0)
        p3 = IntegerPoint(6, 4)
        t1 = IntegerOrthoRightTriangle(p1, p2, p3)
        self.assertEqual(t1.containing_pt_ct(), 19)
        
    def test_containing_pt_ct_no_points_on_hypotenuse(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(7, 0)
        p3 = IntegerPoint(7, 4)
        t1 = IntegerOrthoRightTriangle(p1, p2, p3)
        self.assertEqual(t1.containing_pt_ct(), 21)
        
class TestIntegerOrthoRectangleMethods(unittest.TestCase):
    
    def test_default_initialization(self):
        r1 = IntegerOrthoRectangle()
        self.assertTrue(r1._p1.tuple() == (0, 0) and 
                        r1._p3.tuple() == (0, 0))
        
    def test_creation_from_tuple(self):
        r1 = IntegerOrthoRectangle(p1 = (0, 0), p3 = (2, 2))
        self.assertTupleEqual(r1.vertex_tuple(), ((0, 0), (2, 2)))
        
    def test_repr(self):
        p1 = IntegerPoint(0, 0)
        p3 = IntegerPoint(2, 2)
        r1 = IntegerOrthoRectangle(p1, p3)
        self.assertEqual(repr(r1), '(0, 0)->(2, 0)->(2, 2)->(0, 2)')
        
    def test_vertices(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 2)
        p4 = IntegerPoint(0, 2)
        r1 = IntegerOrthoRectangle(p1, p3)
        self.assertTupleEqual(r1.vertices(), (p1, p2, p3, p4)) 
        
    def test_sides(self):
        p1 = IntegerPoint(0, 0)
        p2 = IntegerPoint(2, 0)
        p3 = IntegerPoint(2, 2)
        p4 = IntegerPoint(0, 2)
        a = IntegerSegment(p1, p2)
        b = IntegerSegment(p2, p3)
        c = IntegerSegment(p3, p4)
        d = IntegerSegment(p4, p1)
        r1 = IntegerOrthoRectangle(p1, p3)
        self.assertTupleEqual(r1.sides(), (a, b, c, d))
    
    def test_containing_pt_ct(self):
        p1 = IntegerPoint(0, 0)
        p3 = IntegerPoint(2, 2)
        r1 = IntegerOrthoRectangle(p1, p3)
        self.assertEqual(r1.containing_pt_ct(), 9)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()