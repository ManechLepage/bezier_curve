import bezier
import arcade
from numpy import array as a

WIDTH = 800
HEIGHT = 600
TITLE = "Bezier Curve"


arcade.open_window(WIDTH, HEIGHT, TITLE)
arcade.set_background_color((51, 51, 51))
arcade.start_render()
curve = bezier.CubicBezier(a([0, 0]), a([200, 600]), a([600, 0]), a([800, 600]))
curve.t = 0.001
pX, pY = curve.calc_points()
for i in range(len(pX)):
    arcade.draw_point(pX[i], pY[i], (255, 255, 255), 5)
arcade.finish_render()
arcade.run()
