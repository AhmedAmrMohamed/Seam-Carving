import numpy as np
from PIL import Image

class Imager:
    ''' handles the all the related image proceesing stuff'''
    def __init__(self,orgPath):
        self.orgPath  = orgPath
        self.img      = self.open()
        self.h,self.w = len(self.img),len(self.img[0])

    def open(self):
        '''open the image into an numpy array'''
        image = Image.open(self.orgPath)
        print(image.size)
        data  = np.array(image)
        return data

    def close(self,path):
        ''' save the img in path '''
        Image.fromarray(self.img).save(path)
    
    def valid (self,pixelv,pixelh):
        validv = pixelv >=0 and pixelv < self.h
        validh = pixelh >=0 and pixelh < self.w
        return validv and validh
    
    def setpixel(self,pixelv,pixelh,rgb):
        ''' set the value of a pixel as [r,g,b] '''
        # np.put(self.img,[pixelx,pixely],[r,g,b])
        # np.put(self.img,[pixelx,pixely],[r,g,b])
        self.img[pixelv,pixelh,0] = rgb[0]
        self.img[pixelv,pixelh,1] = rgb[1]
        self.img[pixelv,pixelh,2] = rgb[2]

    def getpixel(self,pixelv,pixelh):
        ''' get the value of a pixel '''
        if not self.valid(pixelv,pixelh):
            return (0,0,0)
        ret =  self.img[pixelv][pixelh]
        return tuple(map(int,(ret[0],ret[1],ret[2])))
    
    def removeSeam(self,seam):
        ''' 
        remove the the pixels refered to by seam
        by shifting adjacent pixels into their place
        '''
        width = self.w
        gp    = self.getpixel
        sp    = self.setpixel
        for v,h in seam:
            for i in range(h+1,width):
                sp(v,i-1,gp(v,i-1))


    def getEnergy(self,pixelv,pixelh):
        dv = [ 0, 0,-1, 1]
        dh = [-1, 1, 0, 0]
        le,ri,do,up = ((pixelv+a,pixelh+b) for a,b in zip(dv,dh))
        le = self.getpixel(le[0],le[1])
        ri = self.getpixel(ri[0],ri[1])
        do = self.getpixel(do[0],do[1])
        up = self.getpixel(up[0],up[1])

        dh = ((a-b)**2 for a,b in zip(le,ri))
        dv = ((a-b)**2 for a,b in zip(up,do))

        return sum(dh)+sum(dv)
        


from vars import *
def test_open():
    ob = Imager(new)
    print(len(ob.img[0]))
    print(ob.w,ob.h)
    print(ob.img[0][0])
    return ob

def test_close():
    ob = Imager('imgs/surforg.jpeg')
    ob.close('imgs/surfnew.jpeg')

def test_setpixel():
    ob=Imager(org)
    print('org' , ob.getpixel(1,1) )
    ob.setpixel(1,1,255,255,255)
    print('new' , ob.getpixel(1,1) )

def test_setpixel2():
    ob = Imager(low)
    print(ob.h)
    for i in range(ob.w):
            ob.setpixel(0,i,[0,0,0])
    for i in range(ob.h):
            ob.setpixel(i,0,[255,255,255])
    ob.close(new)
def test_removeseam():
    ob = Imager(org)
    seam = [400 for i in range(ob.h-2)]
    for i in range(50):
        print(i)
        ob.removeSeam(seam)
    ob.close('imgs/1.jpeg')

def test_calcenergy():
    ob = Imager(org)
    for i in range(ob.w-1):
        for j in range(ob.h-1):
            print(ob.calcEnergy(j,i))
def test_valid():
    ob = Imager(low)
    assert ob.valid(0,0)
    assert not ob.valid(-1,0)
    assert not ob.valid(0,-1)

def test_getEnergy():
    ob = Imager(muf)
    sv = Imager('imgs/en.jpeg')
    for i in range(ob.w):
        for j in range(ob.h):
            sv.setpixel(j,i,[ob.getEnergy(j,i),0,0])
    sv.close('imgs/en.jpeg')

# test_open()
#test_close()
# test_setpixel2()
#test_removeseam()
# test_calcenergy()
test_getEnergy()
# test_valid()

