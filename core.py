from imager import Imager
import vars
import os
class Core:
    def __init__(self,image):
        self.image = image
    
    def DP(self):
        img   = self.image
        GE    = self.image.getEnergy
        VA    = self.image.valid
        table = [[(0,0) for i in range(img.w)] for i in range(img.h)]
        dh    = (-1,0,1)
        for h in range(img.w):
            for v in range(1,img.h):
                mi = vars.inf
                for sh in dh:
                    nh = h+sh
                    if VA(v-1,nh):
                        t = GE(v-1,nh)
                        if t < mi:
                            mi = t
                            table[v][h] = mi,sh
        return table

    def buildseam(self,table):
        h = 0
        mx = 0
        hi = self.image.h
        for e,i in enumerate(table[hi-1]):
            if i[0] > mx:
                h = e
        li = []
        for v in range(hi-1,-1,-1):
            li.append((v,h))
            h+= table[v][h][1]
        return li


image= Imager(vars.muf)
def test_dp():
    ob = Core(image)
    print('dp...')
    return ob.buildseam(ob.DP())

x = test_dp()

def test_colorseam(x):
    for a,b in x:
        image.setpixel(a,b,[255,255,255])
    image.close('imgs/coloroneseam.jpeg')
test_colorseam(x)


