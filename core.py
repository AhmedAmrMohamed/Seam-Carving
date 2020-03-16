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
        for v in range(img.h-1,-1,-1):
            for h in range(img.w):              
                ge = GE(v,h)
                mi = vars.inf,0
                for sh in (-1,0,1):             
                    if VA(v+1,h+sh):
                        tm = table[v+1][h+sh][0]
                        if tm < mi[0]:
                            mi = tm,sh
                if mi[0] < vars.inf:
                    table[v][h] = ge+mi[0],mi[1]
        return table

    def buildseam(self,table):
        mi = vars.inf,0
        for i in range(self.image.w):
            print(table[0][i][0])
            if mi[0] > table[0][i][0]:
                mi = table[0][i][0],i
        h = i
        li = [(0,i)]
        for v in range(1,self.image.h):
            h += table[v][h][1]
            li.append((v,h))
        return li


def test_dp(image):
    image = Imager(image)
    ob = Core(image)
    print('dp...')
    return ob.buildseam(ob.DP())
x = test_dp('imgs/coloroneseam.jpeg')
im = 'imgs/coloroneseam.jpeg'
def test_colorseam(x,im):
    image = Imager(im)
    for a,b in x:
        image.setpixel(a,b,[255,255,255])
    image.close(im)
test_colorseam(x,im)


