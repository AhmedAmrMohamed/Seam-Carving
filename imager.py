from PIL import Image

class Imager:
    ''' handles the all the related image proceesing stuff'''
    def __init__(self,orgPath,destPath):
        self.orgPath    = orgPath
        self.destPath   = destPath
        self.image      = Image.open(orgPath)
        self.hs,self.vs = self.image.size
        self.table      = self.totable()
        self.entab      = self.buildEnergy()

    def reset(self):
        self.entab = self.buildEnergy()

    def totable(self):
        ''' convert the pick into a table of pixels '''
        print('converting to table...')
        img = self.image
        table = [[ img.getpixel((j,i))for i in range(self.vs)] for j in range(self.hs)]
        print('converted.')
        return table

    def close(self,table=None):
        ''' save the img in path '''
        print('closing...')
        table = table if table else self.table
        copy = self.image.copy()
        for i in range(self.hs-1):
            for j in range(self.vs-1):
                try:
                    pixel = self.table[i][j]
                except Exception as ex:
                    print(f'{ex},{i},{j},{self.hs},{self.vs}')
                copy.putpixel((i,j),pixel)
        copy.save(self.destPath)

    def validPixel(self,pixel):
        a = pixel[0] >= 0 and pixel[0] < self.hs
        b = pixel[1] >= 0 and pixel[1] < self.vs
        return a and b
    
    def getPixel(self,pixel):
        if not self.validPixel(pixel):
            return (0,0,0)
        return self.table[pixel[0]][pixel[1]]

    def setPixel(self,pixel,color):
        self.table[pixel[0]][pixel[1]] = color

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
        
    def removeSeam(self,seam):
        print('removing seam...')
        for x,y in enumerate(seam):
            for j in range(y+1,self.hs):
                self.table[j-1][x] = self.table[j][x]
        self.hs -=1 
        self.reset()
        self.close()
        
    

# from vars import *

# img = Imager(org)
# def test_toarray():
    # return img.toarray()
# def test_close():
    # img.close(path+'testclose.jpg')
# def test_energy():
    # img = Imager(hed,'imgs/ene.jpeg')

