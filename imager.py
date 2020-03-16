from PIL import Image

class Imager:
    ''' handles the all the related image proceesing stuff'''
    def __init__(self,orgPath,destPath):
        self.orgPath    = orgPath
        self.image      = Image.open(orgPath)
        self.hs,self.vs = self.image.size
        self.table      = self.totable()
        self.entab      = self.buildEnergy()
        self.close(self.entab,destPath)

    def totable(self):
        ''' convert the pick into a table of pixels '''
        print('converting to table...')
        img = self.image
        table = [[ img.getpixel((j,i))for i in range(self.vs)] for j in range(self.hs)]
        print('converted.')
        return table

    def close(self,table,path):
        ''' save the img in path '''
        print('closing...')
        copy = self.image.copy()
        for i in range(self.hs-1):
            for j in range(self.vs-1):
                try:
                    pixel = table[i][j]
                except Exception as ex:
                    print(f'{ex},{i},{j},{self.hs},{self.vs}')
                copy.putpixel((i,j),pixel)
        copy.save(path)

    def validPixel(self,pixel):
        a = pixel[0] >= 0 and pixel[0] < self.hs
        b = pixel[1] >= 0 and pixel[1] < self.vs
        return a and b
    
    def getPixel(self,pixel):
        if not self.validPixel(pixel):
            return (0,0,0)
        return self.table[pixel[0]][pixel[1]]

    def getPixelEnergy(self,pixel):
        dv = [ 0, 0,-1, 1]
        dh = [-1, 1, 0, 0]
        le,ri,do,up = (self.getPixel((pixel[0]+a,pixel[1]+b)) for a,b in zip(dv,dh))

        dh = ((a-b)**2 for a,b in zip(le,ri))
        dv = ((a-b)**2 for a,b in zip(up,do))

        return sum(dh)+sum(dv)
    def buildEnergy(self):
        table = [[ self.getPixelEnergy((j,i))for i in range(self.vs)] for j in range(self.hs)]
        return table
        
        
    
    # def valid (self,pixelv,pixelh):
        # validv = pixelv >=0 and pixelv < self.h
        # validh = pixelh >=0 and pixelh < self.w
        # return validv and validh
    
    # def setpixel(self,pixelv,pixelh,rgb):
        # ''' set the value of a pixel as [r,g,b] '''
        # self.img[pixelv,pixelh,0] = rgb[0]
        # self.img[pixelv,pixelh,1] = rgb[1]
        # self.img[pixelv,pixelh,2] = rgb[2]

    # def getpixel(self,pixelv,pixelh):
        # ''' get the value of a pixel '''
        # if not self.valid(pixelv,pixelh):
            # return (0,0,0)
        # ret =  self.img[pixelv][pixelh]
        # return tuple(map(int,(ret[0],ret[1],ret[2])))
    
    # def removeSeam(self,seam):
        # ''' 
        # remove the the pixels refered to by seam
        # by shifting adjacent pixels into their place
        # '''
        # width = self.w
        # gp    = self.getpixel
        # sp    = self.setpixel
        # for v,h in seam:
            # for i in range(h+1,width):
                # sp(v,i-1,gp(v,i-1))


    # def getEnergy(self,pixelv,pixelh):
        # dv = [ 0, 0,-1, 1]
        # dh = [-1, 1, 0, 0]
        # le,ri,do,up = ((pixelv+a,pixelh+b) for a,b in zip(dv,dh))
        # le = self.getpixel(le[0],le[1])
        # ri = self.getpixel(ri[0],ri[1])
        # do = self.getpixel(do[0],do[1])
        # up = self.getpixel(up[0],up[1])

        # dh = ((a-b)**2 for a,b in zip(le,ri))
        # dv = ((a-b)**2 for a,b in zip(up,do))

        # return sum(dh)+sum(dv)
        


from vars import *

# img = Imager(org)
def test_toarray():
    return img.toarray()
def test_close():
    img.close(path+'testclose.jpg')
def test_energy():
    img = Imager(org,'imgs/ene.jpeg')

x=test_energy() 
