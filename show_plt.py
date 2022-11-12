from numpy import array as a
import matplotlib.pyplot as plt
import bezier


def create_bezier(p0, p1, p2, p3):
    points = [p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]]
    plt.plot(points[0], points[1], 'ro')
    plt.plot(points[0], points[1], 'r--')
    curve = bezier.CubicBezier(p0, p1, p2, p3)
    pX, pY = curve.calc_points()
    plt.plot(pX, pY, 'b', linewidth=5)
    plt.show()
