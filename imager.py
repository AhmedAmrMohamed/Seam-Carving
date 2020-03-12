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
        validv = lambda a: True if a>0 and a < self.h else False
        validh = lambda a: True if a>0 and a < self.w else False
        return validv(pixelv) and validh(pixelh)
    
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
            return [0,0,0]
        return self.img[pixelv][pixelh]
    
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
        pixelx = pixelh
        pixely = pixelv
        gp = self.getpixel
        up = gp(pixelx  ,pixely-1)
        do = gp(pixelx  ,pixely+1)
        ri = gp(pixelx+1,pixely  )
        le = gp(pixelx-1,pixely  )

        upr,upg,upb = map(int,(up[0],up[1],up[2]))
        dor,dog,dob = map(int,(do[0],do[1],do[2]))
        rir,rig,rib = map(int,(ri[0],ri[1],ri[2]))
        ler,leg,leb = map(int,(le[0],le[1],le[2]))
        
        dv = (upr-dor)**2 + (upg-dog)**2 + (upb-dob)**2
        dh = (rir-ler)**2 + (rig-leg)**2 + (rib-leb)**2
        
        return dv+dh
        


org  = 'imgs/surforg.jpeg'
new  = 'imgs/surfnew.jpeg'

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
    ob = Imager(org)
    print(ob.h)
    for i in range(ob.w):
            ob.setpixel(0,i,[0,0,0])
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


# test_open()
#test_close()
test_setpixel2()
#test_removeseam()
# test_calcenergy()
