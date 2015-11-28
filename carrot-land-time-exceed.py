__author__ = 'shengwen'
# The carrots may only be planted at points with integer coordinates on the 2-D plane.
# They must lie within the plot of land and not on the boundaries. For example,
# if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).
#  when given a list of three vertices, returns the maximum number of carrots you can plant.
# The three vertices will not be collinear.

#vertices = [[2, 3], [6, 9], [10, 160]]
# Output:
#     (int) 289

vertices = [[91207, 89566], [-88690, -83026], [67100, 47194]]
# Output:
#     (int) 1730960165
# time exeed
def answer(vertices):
    # your code here
    xMin, yMin, xMax, yMax = None, None, None, None
    for i in vertices:
        if xMin == None or xMin > i[0]:
            xMin = i[0]
        if xMax == None or xMax < i[0]:
            xMax = i[0]
        if yMin == None or yMin > i[1]:
            yMin = i[1]
        if yMax == None or yMax < i[1]:
            yMax = i[1]
    p0x, p0y = vertices[0]
    p1x, p1y = vertices[1]
    p2x, p2y = vertices[2]
    Area = 1.0/2*(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y)
    count = 0
    for px in range(xMin, xMax + 1):
        for py in range(yMin, yMax + 1):
            s = 1.0/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py)
            t = 1.0/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py)
            if 0 < s and s < 1 and 0 < t and t < 1 and s + t < 1:
                count += 1
    return count

print answer(vertices)