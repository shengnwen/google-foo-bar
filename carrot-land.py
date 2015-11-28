__author__ = 'shengwen'
# The carrots may only be planted at points with integer coordinates on the 2-D plane.
# They must lie within the plot of land and not on the boundaries. For example,
# if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).
#  when given a list of three vertices, returns the maximum number of carrots you can plant.
# The three vertices will not be collinear.

vertices = [[2, 3], [6, 9], [10, 160]]
# Output:
#     (int) 289

# vertices = [[0, 0],[4, 0], [0, 4]]
# Output:
#     (int) 1730960165
# time exeed
# vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)

def answer(vertices):
    # your code here
    # use pick's algorithm: A = i + B/2 - 1
    p0x, p0y = vertices[0]
    p1x, p1y = vertices[1]
    p2x, p2y = vertices[2]
    _2Area = (-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    b1 = gcd(p0y - p1y, p0x - p1x)
    b2 = gcd(p0y - p2y, p0x - p2x)
    b3 = gcd(p1y - p2y, p1x - p2x)
    B = b1 + b2 + b3
    # calculate boundary points
    return (_2Area + 2 - B)/2


print answer(vertices)