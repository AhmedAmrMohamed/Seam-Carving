from imager import Imager
import vars
import os
class Core:
    def __init__(self,image):
        self.image = image
            
    def DP(self):
        print('building dp...')
        img   = self.image
        ET    = img.entab
        VA    = self.image.validPixel
        table = [[ (0,0)for i in range(img.vs)] for j in range(img.hs)]
        dh    = (-1,0,1)
        for v in range(img.vs-1,-1,-1):
            for h in range(img.hs):              
                ge = ET[h][v]
                mi = vars.inf,0
                for sh in (-1,0,1):             
                    if VA((h+sh,v+1)):
                        tm = table[h+sh][v+1][0]
                        if tm < mi[0]:
                            mi = tm,sh
                if mi[0] < vars.inf:
                    table[h][v] = ge+mi[0],mi[1]
        return table

    def buildseam(self,table):
        print('building seam...')
        mi = vars.inf,0
        for i in range(self.image.hs):
            if mi[0] > table[i][0][0]:
                mi = table[i][0][0],i
        h  = mi[1]
        li = []
        for i in range(0,self.image.vs-1):
            try:
                li.append(h)
                h+= table[h][i][1]
            except Exception as e:
                print(e,i,h)
                quit()
        return li
        




image = Imager('imgs/testdp.jpeg','imgs/testdp.jpeg')
ob = Core(image)
for i in range(100):
        print(i)
        seam = ob.buildseam(ob.DP())
        ob.image.removeSeam(seam)
        

# def test_dp():
    # ob = Core(image)
    # print('dp...')
    # return ob.buildseam(ob.DP())
# x = test_dp()
# def test_colorseam(x):
    # for a,b in enumerate(x):
        # try:
            # image.setPixel((b,a),(255,255,255))
        # except Exception as e:
            # print(e,b,a)
    # image.close()
# test_colorseam(x)


