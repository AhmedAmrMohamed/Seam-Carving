# image = Imager('imgs/hs.jpeg','imgs/hs.jpeg')
# ob = Core(image)
# for i in range(300):
        # print(i)
        # seam = ob.buildseam(ob.DP())
        # ob.image.removeSeam(seam)
import imager
import core
 
def main():
    org = input('path to the target image : ')
    new = input('path to save the result  : ' )
    loo = int(input('how far you want to reduce the image : '))
    
    imob = imager.Imager(org,new)
    coob = core.Core(imob)
    build  = coob.buildseam
    remove = coob.image.removeSeam
    dp     = coob.DP
    for i in range(loo):
        print(i)
        seam = build(dp())
        remove(seam)
 
main()
        
