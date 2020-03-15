from imager import Imager
import vars
import os
class Core:
    def __init__(self,image):
        self.image = image
    
    def getSeam(self):
        ''' return the seam with the lowest energy '''
        memo = {}
        mi = vars.inf,[]
        for i in range(self.image.w):
            po,li = self.getSeamof((0,i),memo)
            if po < mi[0]:
                mi = po,li
            print(i,po)
        return po,li
            

    def getSeamof(self,pixel,memo):
        ''' return the seam with the lowest energy starting at `pixel` '''
        dh  = [-1,0,1]
        # print(pixel)
        img = self.image
        track = [0 for i in range(img.h)]
        hig = img.h
        def calc(pixel):
            print(pixel)
            ret = memo.get(pixel,None)
            if ret:
                return ret
            pv = pixel[0]
            if pv == img.h:
                return 0
            if not img.valid(pixel[0],pixel[1]):
                return 1<<32
            ret = image.getEnergy(pv,pixel[1])
            mi = vars.inf
            for sh in dh:
                ph = pixel[1]+sh
                tmp = calc((pv+1,ph))
                if tmp < mi:
                    mi = tmp
                    track[pv]=sh
            ret += mi
            memo[pixel]  = ret
            return ret 
        return calc(pixel),track
                    


os.sys.setrecursionlimit(100000000)

image= Imager(vars.org)
def test_getseamof():
    ob = Core(image)
    print('mt')
    return ob.getSeamof((0,100),{})
def test_getseam():
    ob = Core(image)
    return ob.getSeam()

def test_colorseam(x):
    pv,ph = 0,0
    for i in x:
        ph+=i
        image.setpixel(pv,ph,[255,255,255])
        pv+=1
    image.close('imgs/coloroneseam.jpeg')

x = test_getseamof()
test_colorseam(x[1])

