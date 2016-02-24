'''
Created on Jan 30, 2016

@author: grovesr

google foo.bar challenge 4.1

Carrotland
==========

The rabbits are free at last, free from that horrible zombie science 
experiment. They need a happy, safe home, where they can recover.

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and
columns! But first, you need some land. And the only person who's selling land
is Farmer Frida. Unfortunately, not only does she have only one plot of land,
she also doesn't know how big it is - only that it is a triangle. However, she
can tell you the location of the three vertices, which lie on the 2-D plane and
 have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to
follow these guidelines: The carrots may only be planted at points with integer
coordinates on the 2-D plane. They must lie within the plot of land and not on
the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1),
then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices,
returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will 
be a list of two integers representing the x and y coordinates of a vertex. 
All coordinates will have absolute value no greater than 1000000000. The three 
vertices will not be collinear.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) vertices = [[2, 3], [6, 9], [10, 160]]
Output:
    (int) 289

Inputs:
    (int) vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
Output:
    (int) 1730960165
'''
from math import sqrt
from fractions import Fraction
from decimal import  Decimal
class IntegerPoint():
    '''
    IntegerPoint object
    '''
    
    def __init__(self, x = None, y = None):
        if x is not None and y is not None:
            self._x = int(x)
            self._y = int(y)
        else:
            self._x = 0
            self._y = 0
    
    def __repr__(self):
        return '(%d, %d)' % (self._x, self._y)
    
    def __sub__(self, other):
        return IntegerPoint(self._x - other._x, self._y - other._y)
    
    def __add__(self, other):
        return IntegerPoint(self._x + other._x, self._y + other._y)
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._x == other._x and self._y == other._y
    
    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._x != other._x or self._y != other._y
    
    def touches_edge(self, edge):
        intercept = edge._p1._y - edge.slope() * edge._p1._x
        return edge.slope() * self._x + intercept == self._y
    
    def relation_to_line(self, line):
        '''
        check to see if this point is greater than the line. 
        equation of line y - mx - b  = result
        if result == 0 then point is on this line when stretched to
        infinity.  Sign of result indicates location of point on one side 
        or other of this line.
        '''
        b = line._p1._y - line.slope() * line._p1._x
        m = line.slope()
        if m == float('inf'):
            result = self._x - line._p1._x
        else:
            result = self._y - m * self._x - b
        if result == 0:
            return 0
        return result / abs(result)
    
    def tuple(self):
        return (self._x, self._y)
    
class IntegerSegment():
    '''
    IntegerSegment object
    consists of two IntegerPoints
    '''
    
    def __init__(self, p1 = None, p2 = None):
        if (isinstance(p1, tuple) and isinstance(p2,tuple)  and 
            len(p1) == 2 and len(p2) == 2):
            self._p1 = IntegerPoint(p1[0], p1[1])
            self._p2 = IntegerPoint(p2[0], p2[1])
        elif p1 is not None and p2 is not None:
            self._p1 = p1
            self._p2 = p2
        else:
            self._p1 = IntegerPoint(0, 0)
            self._p2 = IntegerPoint(0, 0)
    
    def __repr__(self):
        return '%s->%s' % (str(self._p1), str(self._p2))
        
    def slope(self):
        delta = self._p2 - self._p1
        try:
            m = Fraction(delta._y, delta._x)
        except ZeroDivisionError:
            m = float('inf')
        return m
            
    def length(self):
        delta = self._p2 - self._p1
        return sqrt(delta._y**2 + delta._x**2)
    
    def ortho(self):
        return self.slope() == 0 or self.slope() == float('inf')
    
    def vertices(self):
        return (self._p1, self._p2)
    
    def other_end_point(self, point):
        return [endPoint for endPoint in self.vertices() if endPoint != point][0]
    
    def contains_point(self, point):
        return self._p1 == point or self._p2 == point
    
    def intersects_triangle(self, triangle):
        '''
        This edge crosses the interior space of a triangle.
        
        If all triangle vertices have same relationship to self and are 
        non-zero, the line doesn't cross the triangle.  
        
        From http://stackoverflow.com/a/3590421
        
        If the triangle has a vertex interior to the circumscribing rectangle, 
        then the line stretched to infinity may cross the triangle, but the 
        line segment may still not enter the triangle interior.
        Check to see if the line SEGMENT has points on either side of the triangle
        long edge.  If it does, the line crosses the triangle.
        '''
        signs = set()
        interiorPoint = triangle.pt_inside_circumscribing_rectangle()
        if interiorPoint:
            # Checking for cases where the triangle contains a 
            # vertex inside the circumscribing rectangle.
            # Check if this line segment has points on both sides of the 
            # triangle long edge.  If it dies, this line crosses the triangle
            longEdge = triangle.long_edge()
            signs = set()
            for point in self.vertices():
                signs.add(point.relation_to_line(longEdge))
        else:
            for point in triangle.vertices():
                signs.add(point.relation_to_line(self))
        return -1 in signs and 1 in signs
        
    def tuple(self):
        return(self._p1.tuple(), self._p2.tuple())
    
    def like(self, other):
        commonPoints = [point for point in self.vertices() 
                        if point in other.vertices()]
        return len(commonPoints) == 2
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False 
        return self.vertices() == other.vertices()
    
    def __ne__(self, other):
        if not isinstance(other, self.__class__):
            return False 
        return self.vertices() != other.vertices()

    def containing_pt_ct(self):
        '''
        containing_pt_ct returns number of points on a 2-D, integer
        cartesian plane that touch the IntegerSegment lying in that plane.
        '''
        if self.length() == 0:
            pointCount = 1
        if self.slope() == float('inf'):
            pointCount = abs((self._p2 - self._p1)._y) + 1
        elif self.slope() == 0:
            pointCount = abs((self._p2 - self._p1)._x) + 1
        else:
            delta = self._p2 - self._p1
            pointCount =  abs(delta._x / self.slope().denominator) + 1
        return pointCount

class IntegerTriangleError(): pass

class IntegerTriangle(object):
    '''
    IntegerTriangle object
    consists of three IntegerPoints
    '''
    def __init__(self, p1 = None, p2 = None, p3 = None):
        if (isinstance(p1, tuple) and isinstance(p2,tuple)  and 
            isinstance(p3,tuple)  and len(p1) == 2 and len(p2) == 2 and
            len(p3) == 2):
            self._p1 = IntegerPoint(p1[0], p1[1])
            self._p2 = IntegerPoint(p2[0], p2[1])
            self._p3 = IntegerPoint(p3[0], p3[1])
        elif p1 is not None and p2 is not None and p3 is not None:
            self._p1 = p1
            self._p2 = p2
            self._p3 = p3
        else:
            self._p1 = IntegerPoint(0, 0)
            self._p2 = IntegerPoint(0, 0)
            self._p3 = IntegerPoint(0, 0)
        self._a = IntegerSegment(self._p1, self._p2)
        self._b = IntegerSegment(self._p2, self._p3)
        self._c = IntegerSegment(self._p3, self._p1)
        
    def __repr__(self):
        return '%s->%s->%s' % (str(self._p1), str(self._p2), str(self._p3))
    
    def vertices(self):
        return (self._p1, self._p2, self._p3)
    
    def sides(self):
        return (self._a, self._b, self._c)
    
    def vertex_tuple(self):
        return (self._p1.tuple(), self._p2.tuple(), self._p3.tuple())
    
    def side_tuple(self):
        return (self._a.tuple(), self._b.tuple(), self._c.tuple())
    
    def is_ortho(self):
        return self._a.ortho() or self._b.ortho() or self._c.ortho()
    
    def is_ortho_right(self):
        return ((self._a.ortho() and self._b.ortho()) or
                (self._a.ortho() and self._c.ortho()) or
                (self._b.ortho() and self._c.ortho()))
    
    def minx(self):
        return min([p._x for p in self.vertices()])
    
    def miny(self):
        return min([p._y for p in self.vertices()])
    
    def maxx(self):
        return max([p._x for p in self.vertices()])
    
    def maxy(self):
        return max([p._y for p in self.vertices()])
    
    def like(self, other):
        return len([point for point in self.vertices() 
                    if point in other.vertices()]) == 3 
    
    def long_edge(self):
        longEdge = self.sides()[0]
        for edge in self.sides():
            if edge.length() > longEdge.length():
                longEdge = edge
        return longEdge
    
    def interior_edges_tuple(self):
        '''
        return edge tuples not coincident with an edge of the circumscribed 
        rectangle
        '''
        interiorEdges = set()
        circumscribedRectangle = self.circumscribed_rectangle()
        for triSide in self.sides():
            found = False
            for rectSide in circumscribedRectangle.sides():
                if triSide.like(rectSide):
                    found = True
                    break
            if not found:
                interiorEdges.add(triSide.tuple())
        return list(interiorEdges)
                
    def interior_edges(self):
        return [IntegerSegment(edgeTuple[0], edgeTuple[1]) 
                for edgeTuple in self.interior_edges_tuple()]
        
    def pt_inside_circumscribing_rectangle(self):
        pts = [point for point in self.vertices() 
                if point._x > self.minx() and point._x < self.maxx() and 
                point._y > self.miny() and point._y < self.maxy()]
        if pts:
            return pts[0]
        return None
    
    def circumscribed_rectangle(self):
        return IntegerOrthoRectangle(IntegerPoint(self.minx(), self.miny()), 
                                     IntegerPoint(self.maxx(), self.maxy()))
    
    def squaring_triangles(self):
        squaringTriangles = []
        interiorEdges = self.interior_edges()
        interiorPoint = self.pt_inside_circumscribing_rectangle()
        # return the surrounding triangles to rectangularize the triangle
        for interiorEdge in interiorEdges:
            touchingPoints = self.circumscribed_rectangle().points_touching(interiorEdge)
            if len(touchingPoints) == 1:
                # try to create an ortho right triangle from the end of the interior
                # edge that doesn't touch a vertex of the circumscribing rectangle.
                # Make sure you create the triangle that doesn't cross self
                otherEndPoint = touchingPoints[0]
                firstEndPoint =interiorEdge.other_end_point(touchingPoints[0])
            elif len(touchingPoints) == 1:
                # this is the special case of the interior edge running
                # between diagonal corners of the circumscribing rectangle
                otherEndPoint = touchingPoints[1]
                firstEndPoint = touchingPoints[0]
            else:
                # no touching points
                firstEndPoint = interiorEdge._p1
                otherEndPoint = interiorEdge._p2
            popt = IntegerPoint(firstEndPoint._x, 
                                otherEndPoint._y)
            newEdge = IntegerSegment(firstEndPoint, popt)
            pointValid = not newEdge.intersects_triangle(self)
            if interiorPoint and len(touchingPoints) == 2:
                # check to see if popt lies on the opposite side of the 
                # diagonal interior edge as the interiorPoint.  If it doesn't 
                # don't create this triangle, otherwise it will overlap self
                pointValid = (popt.relation_to_line(interiorEdge) != 
                              interiorPoint.relation_to_line(interiorEdge))
            newTriangle = IntegerOrthoRightTriangle(otherEndPoint, 
                                                        firstEndPoint, 
                                                        popt)
            if not pointValid or newTriangle.like(self):
                # try the other direction
                popt  = IntegerPoint(otherEndPoint._x,
                                     firstEndPoint._y)
                newTriangle = IntegerOrthoRightTriangle(otherEndPoint, 
                                                        firstEndPoint, 
                                                        popt)
            squaringTriangles.append(newTriangle)
        return squaringTriangles
    
    def squaring_shapes(self):
        '''
        Set of shapes that are added to the exterior of the triangle to fill up 
        the circumscribed rectangle.  Will be three right triangles and 
        possibly a rectangle.
        '''
        squaringShapes = self.squaring_triangles()
        interiorPoint = self.pt_inside_circumscribing_rectangle()
        if interiorPoint:
            # we have to include a surrounding rectangle to the three triangles 
            # to rectangularize the triangle
            longEdge = self.long_edge()
            nonTouchingPoints = self.circumscribed_rectangle().points_not_touching(longEdge)
            for point in nonTouchingPoints:
                if (point.relation_to_line(longEdge) == 
                    interiorPoint.relation_to_line(longEdge)):
                    # create the squaring rectangle if the point is on the 
                    # same side of the diagonal edge as interiorPoint
                    squaringShapes.append(IntegerOrthoRectangle(point, interiorPoint))
                    break
        return squaringShapes

    def interior_pt_ct(self):
        '''
        interior_pt_ct returns number of points on a 2-D, integer
        cartesian plane that are interior to the IntegerTriangle lying in that 
        plane.  We find the containing circumscribing rectangle, then locate the
        orthogonal right triangles and possibly an orthogonal rectangle needed 
        to rectangularize the triangle.  We can calculate the containing points
        for rectangles and right triangles easily.  Once we have calculated
        those, we just subtract them from the points inside the circumscribing 
        rectangle to get the points completely interior to this triangle.
        '''
        exteriorPoints=0
        squaringShapes = self.squaring_shapes()
        multiCountPoints = 0
        edgePoints = 0
        uniquePoints = []
        uniqueSides = []
        for shape in squaringShapes:
            for point in shape.vertices():
                if point in uniquePoints:
                    multiCountPoints += 1
                else:
                    uniquePoints.append(point)
            for side in shape.sides():
                if len([sd for sd in uniqueSides if sd.like(side)]) > 0:
                    multiCountPoints += (side.containing_pt_ct() - 2)
                else:
                    uniqueSides.append(side)
        for shape in squaringShapes:
            exteriorPoints += shape.containing_pt_ct()
        exteriorPoints -= multiCountPoints
        circumscribedRectangle = self.circumscribed_rectangle()
        for triSide in self.sides():
            for rectSide in circumscribedRectangle.sides():
                if triSide.like(rectSide):
                    edgePoints += (triSide.containing_pt_ct() - 2)
        if self.is_ortho_right():
            # a common edge point needs to be removed
            edgePoints += 1
        return int(self.circumscribed_rectangle().containing_pt_ct() - 
                exteriorPoints - edgePoints)
    
class IntegerOrthoRightTriangleInvalidError(IntegerTriangleError): pass
    
class IntegerOrthoRightTriangle(IntegerTriangle):
    '''
    IntegerOrthoRightTriangle object consists of three IntegerPoints 
    representing the corners of a right triangle that has two sides parallel
    to the horizontal and vertical axes in a 2D cartesian plane.
    We can easily calculate the containing point count.
    '''
    
    def __init__(self, *args, **kwargs):
        super(IntegerOrthoRightTriangle,self).__init__(*args, **kwargs)
        if not self.is_ortho_right():
                raise IntegerOrthoRightTriangleInvalidError
    
    def containing_pt_ct(self):
        '''
        containing_pt_ct returns number of points on a 2-D, integer
        cartesian plane that are covered by the IntegerOrthoTriangle lying in 
        that plane.
        '''
        hyp = self.interior_edges()[0]
        return (Fraction(self.circumscribed_rectangle().containing_pt_ct(), 2) +
                Fraction(hyp.containing_pt_ct(), 2))

class IntegerOrthoRectangle():
    '''
    IntegerOrthoRectangle object consists of two IntegerPoints  representing
    the diagonally opposed corners of a rectangle that has sides parallel
    to the horizontal and vertical axes in a 2D cartesian plane
    We can easily calculate the containing point count.
    '''
    def __init__(self, p1 = None, p3 = None):
        if p1 == None:
            self._p1 = IntegerPoint(0, 0)
        if p3 == None:
            self._p3 = IntegerPoint(0, 0)
        if (isinstance(p1, tuple) and isinstance(p3,tuple)  and 
            len(p1) == 2 and len(p3) == 2):
            self._p1 = IntegerPoint(p1[0], p1[1])
            self._p3 = IntegerPoint(p3[0], p3[1])
        elif p1 is not None and p3 is not None:
            self._p1 = p1
            self._p3 = p3
        if self._p1 is not None and self._p3 is not None:
            self._a = IntegerSegment(self._p1, IntegerPoint(self._p3._x, self._p1._y))
            self._b = IntegerSegment(IntegerPoint(self._p3._x, self._p1._y), self._p3)
            self._c = IntegerSegment(self._p3, IntegerPoint(self._p1._x, self._p3._y))
            self._d = IntegerSegment(IntegerPoint(self._p1._x, self._p3._y), self._p1)
        
    def __repr__(self):
        return '%s->%s->%s->%s' % self.vertices()
    
    def vertices(self):
        p2 = IntegerPoint(self._p3._x, self._p1._y)
        p4 = IntegerPoint(self._p1._x, self._p3._y)
        return (self._p1, p2, self._p3, p4)
    
    def sides(self):
        return (self._a, self._b, self._c, self._d)
    
    def vertex_tuple(self):
        return (self._p1.tuple(), self._p3.tuple())
    
    def like(self, other):
        return len([point for point in self.vertices() 
                    if point in other.vertices()]) == 4
    
    def points_touching(self, edge):
        return [point for point in self.vertices() 
                if edge.contains_point(point)]
    
    def points_not_touching(self, edge):
        return [point for point in self.vertices() 
                if not edge.contains_point(point)]
    
    def containing_pt_ct(self):
        '''
        containing_pt_ct returns number of points on a 2-D, integer
        cartesian plane that are covered by the IntegerOrthoRectangle lying in 
        that plane.
        '''
        return self._a.containing_pt_ct() * self._b.containing_pt_ct()
    
def answer(vertices):
    '''
    Calculate the number of integer grid points contained completely inside of
    an arbitrary triangle with vertices placed on integer grid points.
    
    I know! I know! Pick's theorem!  I got started down the road of completing
    the circumscribing rectangle by adding orthogonal right triangles and 
    rectangles from which we can easily calculate containing point counts.
    Then all we have to do is subtract these "squaring" shape's containing
    point counts from the circumscribing rectangle containing point count to
    get the interior point count of the triangle.  Sure Pick's theorem is MUCH
    shorter and more efficient, but I like my solution as well!
    
    once I finally figured out that my approach was getting much too involved,
    I started Googling and found Pick's theorem on Wikipedia.  I went ahead
    and finished the "squaring" solution and then implemented Pick's theorem
    too.  It made dealing with the large number float math concerns with 
    Pick's theorem easy, since I had a working solution for arbitrary 
    triangles with my "squaring" solution that I could use to compare.
    
    If your in love with Pick's theorem, just use answer_picks(vertices).  I 
    won't hold it against you :-)
    '''
    p1=IntegerPoint(vertices[0][0], vertices[0][1])
    p2=IntegerPoint(vertices[1][0], vertices[1][1])
    p3=IntegerPoint(vertices[2][0], vertices[2][1])
    triangle = IntegerTriangle(p1, p2, p3)
    return triangle.interior_pt_ct()


# Pick's theorem approach starts here
def slope(p0, p1):
    try:
        m = Fraction(p1[1] - p0[1], p1[0] - p0[0])
    except ZeroDivisionError:
        m = float('inf')
    return m

def edge_points(p0, p1):
    m = slope(p0, p1)
    if m == float('inf'):
        n = abs(p1[1] - p0[1]) + 1
    elif m == 0:
        n = abs(p1[0] - p0[0]) + 1
    else:
        n = abs((p1[0] - p0[0]) / m.denominator) + 1
    return int(n)

def triangle_area(p0, p1, p2):
    lena = Decimal(Decimal(p1[0] - p0[0]) ** 2 + Decimal(p1[1] - p0[1]) ** 2) ** Decimal(0.5)
    lenb = Decimal(Decimal(p2[0] - p1[0]) ** 2 + Decimal(p2[1] - p1[1]) ** 2) ** Decimal(0.5)
    lenc = Decimal(Decimal(p0[0] - p2[0]) ** 2 + Decimal(p0[1] - p2[1]) ** 2) ** Decimal(0.5)
    # 1/2 perimeter
    s = Decimal(0.5) * (lena + lenb + lenc)
    # area (from CRC standard mathematical tables 29th edition)
    k = Decimal(s * (s - lena) * (s - lenb) * (s - lenc)) ** Decimal(0.5)
    return k

def answer_picks(vertices):
    # OK, now that we've done it wrong, let's try using Pick's theorem
    # https://en.wikipedia.org/wiki/Pick's_theorem
    # A = i + b/2 - 1
    # where i is the number of interior points
    # b = the number of edge points
    # call vertices 0, 1, 2
    # call edges a, b, c where:
    # a = 0 -> 1
    # b = 1 -> 2
    # c = 2 -> 0
    na = edge_points(vertices[0], vertices[1])
    nb = edge_points(vertices[1], vertices[2])
    nc = edge_points(vertices[2], vertices[0])
    b = na + nb + nc - 3
    A = triangle_area(vertices[0], vertices[1], vertices[2])
    i = A - b / 2 + 1
    return int(round(i,1))

if __name__ == '__main__':
    vertices = [[2, 3], [6, 9], [10, 160]]
    vertices = [[0, 0], [7, 2], [2, 6]]
    vertices = [[0, 0], [7, 0], [7, 7]]
    vertices = [[0, 0], [9,2], [2, 5]]
#     vertices = [[0, 0], [2, 0], [2, 1]]
#     vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
    print answer_picks(vertices)
#     cProfile.run('answer(vertices)')