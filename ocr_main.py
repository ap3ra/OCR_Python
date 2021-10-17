from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import csv

def loadImage(fichier):
    image = Image.open(fichier)
    return image

def cleanImage(image):
    im_P = image.crop((30,7,590,350))
    return im_P

def scanImage(image):
    img = Image.open(image)
    rgb_im = img.convert('RGB')
    width , height = img.size
    x = []
    y = []
    
    for j in range(width-1):
        for i in range(height-1):
            color = np.array(rgb_im.getpixel((j, i)))
            colorB = np.array([255, 255, 255])
            if (color != colorB).all():
                x.append(j)
                y.append(-i)
    return x,y

def toCSV(x,y):
    fichier = open('courbe.csv', 'w', newline="")
    writer = csv.writer(fichier,delimiter=";",quoting=csv.QUOTE_ALL)
    data = [x,y]
    writer.writerows(zip(*data))
    
            
    fichier.close()


im = loadImage("courbe.png")
imP = cleanImage(im)

imP.save("courbeT.bmp")
x,y = scanImage("courbeT.bmp")
toCSV(x,y)
im.show()
imP.show()

plt.plot(x,y)
plt.axis('off')
plt.show()
