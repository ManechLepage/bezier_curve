import numpy as np


class CubicBezier:

    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.t = 0.01

    def calc_points(self):
        pX = []
        pY = []
        for t in np.arange(0, 1, self.t):
            p = (1 - t) ** 3 * self.p0 + t * self.p1 * (3 * (1 - t) ** 2) + self.p2 * (3 * (1 - t) * t ** 2) + self.p3 * t ** 3
            pX.append(p[0])
            pY.append(p[1])
        return [pX, pY]
