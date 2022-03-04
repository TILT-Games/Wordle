from cmu_graphics import *

s = Star(200,200,100,5)

def onStep():
    s.rotateAngle += 1

cmu_graphics.run()