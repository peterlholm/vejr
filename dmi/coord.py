"Coord calculation"
from pathlib import Path
from PIL import Image

# DMI coords():
#     sw = (52.2942, 18.8932)
#     se = (52.2943, 4.3790)
#     nw = (60.0,3.0)
#     ne = (59.8277, 20.7351)

# pylint: disable=invalid-name

def pixel_pos(start_coord, slut_coord, size, coord):
    "find pixel position of given coordinat where start < slut"
    rel = (coord - start_coord)/(slut_coord-start_coord)
    x = int(rel * size)
    #print ("x", x)
    return x

def radar_pic_cut(img, nw, se, new_nw, new_se):
    "Return image cut with new coordinate"
    #print ("imgshape", img.size)
    pw, ph = img.size
    top = ph - pixel_pos(se[0], nw[0], ph, new_nw[0])
    bund = ph - pixel_pos(se[0], nw[0], ph, new_se[0])
    #print (top, bund)
    left =  pixel_pos(nw[1], se[1], pw, new_nw[1])
    right =  pixel_pos(nw[1], se[1], pw, new_se[1])
    #print (left, right)
    newimg = img.crop((left, top, right, bund))
    return newimg

if __name__=='__main__':
    file = folder = Path(__file__).parent.parent / 'data' / 'radar' / 'dk.com.202211101630.500_max.bw.png'
    myimg = Image.open(file)
    myimg = radar_pic_cut(myimg,  (52.2943, 4.3790), (59.8277, 20.7351), (52.30, 4.38), (54.7, 10.7) )
    myimg.save("test.png")
  