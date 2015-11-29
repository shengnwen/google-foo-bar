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

def lattice_points(p1, p2):
    return gcd(p1[0] - p2[0], p1[1] - p2[1]) - 1



def answer(vertices):
    # your code here
    # use pick's algorithm: A = i + B/2 - 1
    xPoints = [i for i in sorted(vertices, key=lambda x: x[0])]
    yPoints = [i for i in sorted(vertices, key=lambda x: x[1])]
    j = xPoints[-1][0] - xPoints[0][0]
    k = yPoints[-1][1] - yPoints[0][1]
    points = (j - 1) * (k - 1)
    # print "rec:" + str(points)
    for i in range(3):
        va = xPoints[i]
        vb = xPoints[(i + 1)%3]
        vc = xPoints[(i + 2)%3]

        vba_x = abs(va[0] - vb[0])
        vba_y = abs(va[1] - vb[1])

        if vba_x != 0 and vba_y != 0:
            points -= float((vba_x - 1) * (vba_y - 1) - lattice_points(va, vb)) / 2 + lattice_points(va, vb)

        if i == 0 or i == 2 or va[1] == yPoints[0][1] or va[1] == yPoints[-1][1]:
            continue
        k = float(vb[1] - vc[1])/float(vb[0] - vc[0])
        k1 = 0
        k2 = 0
        if va[1] > k * (va[0] - vb[0]) + vb[1]:
            k1 = va[0] - xPoints[0][0]
            k2 = yPoints[-1][1] - va[1]
        else:
            k1 = xPoints[-1][0] - va[0]
            k2 = va[1] - yPoints[0][1]
        points -= k1 * k2
        # print "k1:" + str(k1) + ", k2:" + str(k2)
    return int(points)




print answer(vertices)