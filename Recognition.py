from scipy import misc as sp
from scipy import ndimage
import numpy as np
import pylab as plt
from matplotlib import patches
import math
count = 0

## Image recognition with mickey shapes and cars
def main():
    ## Part 3: filters
    image = sp.imread('toy.png', mode='L')
    image = image.astype(float)
    fil = sp.imread('filter.jpg', mode='L')
    fil = fil.astype(float)
    num = 0
    val = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = 255 - image[x][y]
            num += 1
            val += image[x][y]
    mean = val/num
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] -= mean
            
    num = 0
    val = 0
    
    fil2 = np.copy(fil)

    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil2[x][y] = 255 - fil[x][y]
            num += 1
            val += fil2[x][y]
    mean = val/num
    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil[x][y] = fil2[x][fil.shape[1]-1-y] - mean
    
    out = ndimage.correlate(image, fil)
    plt.imshow(out, cmap='jet')
    plt.show()
    
    max1 = 0
    p1 = 0,0
    max2 = 0
    p2 = 0,0
    max3 = 0
    p3 = 0,0
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            if (out[x][y] > max1 and out[x][y] > max2 and out[x][y] > max3):
                max1 = out[x][y]
                p1 = x,y
            elif (out[x][y] > max2 and out[x][y] > max3):
                max2 = out[x][y]
                p2 = x,y
            elif (out[x][y] > max3):
                max3 = out[x][y]
                p3 = x,y
    
    image = sp.imread('toy.png', mode='L')
    image = image.astype(float)
    
    fig,img = plt.subplots(1)
    box1 = patches.Rectangle((p1[1]-fil.shape[0]/2, p1[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    box2 = patches.Rectangle((p2[1]-fil.shape[0]/2, p2[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    box3 = patches.Rectangle((p3[1]-fil.shape[0]/2, p3[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    img.imshow(image)
    img.add_patch(box1)
    img.add_patch(box2)
    img.add_patch(box3)
    plt.show()
    
    fig,img = plt.subplots(1)   
    box1 = patches.Rectangle((p1[1]-fil.shape[0]/2, p1[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    box2 = patches.Rectangle((p2[1]-fil.shape[0]/2, p2[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    box3 = patches.Rectangle((p3[1]-fil.shape[0]/2, p3[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='b')
    boxt1 = patches.Rectangle((p1[1]-fil.shape[0]/2+10, p1[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='r')
    boxt2 = patches.Rectangle((p2[1]-fil.shape[0]/2+20, p2[0]-fil.shape[1]/2-10),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='r')
    boxt3 = patches.Rectangle((p3[1]-fil.shape[0]/2+20, p3[0]-fil.shape[1]/2),fil.shape[0], fil.shape[1], linewidth=1, facecolor='none', edgecolor='r')
    err1 = boxErr(p1[1]-fil.shape[0]/2, p1[0]-fil.shape[1]/2, p1[1]-fil.shape[0]/2+10, p1[0]-fil.shape[1]/2,fil.shape[0],fil.shape[1])
    err2 = boxErr(p1[1]-fil.shape[0]/2, p1[0]-fil.shape[1]/2, p1[1]-fil.shape[0]/2+20, p1[0]-fil.shape[1]/2-10,fil.shape[0],fil.shape[1])
    err3 = boxErr(p1[1]-fil.shape[0]/2, p1[0]-fil.shape[1]/2, p1[1]-fil.shape[0]/2+30, p1[0]-fil.shape[1]/2, fil.shape[0],fil.shape[1])
    print(err1)
    print(err2)
    print(err3)
    img.imshow(image)
    img.add_patch(box1)
    img.add_patch(box2)
    img.add_patch(box3)
    img.add_patch(boxt1)
    img.add_patch(boxt2)
    img.add_patch(boxt3)
    plt.show()
    
    #3.3 CAR 1
    image = sp.imread('car1.jpg', mode='L')
    image = sp.imresize(image, 0.25)
    image = image.astype(float)
    fil = sp.imread('cartemplate.jpg', mode='L')
    fil = sp.imresize(fil, (int((245-100)/4),int((522-175)/4)))
    fil = fil.astype(float)
    num = 0
    val = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = 255 - image[x][y]
            num += 1
            val += image[x][y]
    mean = val/num
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] -= mean
            
    num = 0
    val = 0
    
    fil2 = np.copy(fil)
    
    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil2[x][y] = 255 - fil[x][y]
            num += 1
            val += fil2[x][y]
    mean = val/num
    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil[x][y] = fil2[x][y] - mean
    
    plt.imshow(fil, cmap='jet')
    plt.show()
    
    out = ndimage.correlate(image, fil)
    plt.imshow(out, cmap='jet')
    plt.show()
    
    max1 = 0
    p1 = 0,0
    max2 = 0
    p2 = 0,0
    max3 = 0
    p3 = 0,0
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            if (out[x][y] > max1):
                max1 = out[x][y]
                p1 = x,y

    image = sp.imread('car1.jpg', mode='L')
    image = sp.imresize(image, 0.25)
    image = image.astype(float)
    
    fig,img = plt.subplots(1)
    box1 = patches.Rectangle((p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2),fil.shape[1], fil.shape[0], linewidth=1, facecolor='none', edgecolor='b')
    img.imshow(image)
    img.add_patch(box1)
    plt.show()
    
    
    fig,img = plt.subplots(1)   
    box1 = patches.Rectangle((p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2),fil.shape[1], fil.shape[0], linewidth=2, facecolor='none', edgecolor='b')
    boxt1 = patches.Rectangle((175/4, 145/4),(522-175)/4, (245-100)/4, linewidth=2, facecolor='none', edgecolor='g')
    err1 = boxErr(p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2, p1[1]-fil.shape[1]/2+10, p1[0]-fil.shape[0]/2,fil.shape[0],fil.shape[1])
    box2 = patches.Rectangle((p1[1]-fil.shape[1]/2, 145/4),(522-175)/4-(522/4-p1[1]-fil.shape[1]/2),(p1[0]+fil.shape[0]/2)-(245-100)/4, linewidth=2, facecolor='none', edgecolor='m')
    print("Accuracy:")
    print(err1)
    img.imshow(image)
    img.add_patch(box1)
    img.add_patch(boxt1)
    img.add_patch(box2)
    plt.show()
    
    # 3.3 Car 2
    image = sp.imread('car2.jpg', mode='L')
    image = sp.imresize(image, 0.25)
    image = image.astype(float)
    fil = sp.imread('cartemplate.jpg', mode='L')
    fil = sp.imresize(fil, (int((357-205)/4), int((488-69)/4)))
    fil = fil.astype(float)
    num = 0
    val = 0
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] = 255 - image[x][y]
            num += 1
            val += image[x][y]
    mean = val/num
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            image[x][y] -= mean
            
    num = 0
    val = 0
    
    fil2 = np.copy(fil)
    
    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil2[x][y] = 255 - fil[x][y]
            num += 1
            val += fil2[x][y]
    mean = val/num
    for x in range(fil.shape[0]):
        for y in range(fil.shape[1]):
            fil[x][y] = fil2[x][fil.shape[1] - y - 1] - mean
    
    plt.imshow(fil, cmap='jet')
    plt.show()
    
    out = ndimage.correlate(image, fil)
    plt.imshow(out, cmap='jet')
    plt.show()
    
    max1 = 0
    p1 = 0,0
    max2 = 0
    p2 = 0,0
    max3 = 0
    p3 = 0,0
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            if (out[x][y] > max1):
                max1 = out[x][y]
                p1 = x,y

    image = sp.imread('car2.jpg', mode='L')
    image = sp.imresize(image, 0.25)
    image = image.astype(float)
    
    fig,img = plt.subplots(1)
    box1 = patches.Rectangle((p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2),fil.shape[1], fil.shape[0], linewidth=2, facecolor='none', edgecolor='b')
    img.imshow(image)
    img.add_patch(box1)
    plt.show()
    
    
    fig,img = plt.subplots(1)   
    box1 = patches.Rectangle((p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2),fil.shape[1], fil.shape[0], linewidth=2, facecolor='none', edgecolor='b')
    boxt1 = patches.Rectangle((69/4, 205/4),(488-69)/4,(357-205)/4, linewidth=2, facecolor='none', edgecolor='g')
    box2 = patches.Rectangle((69/4, 205/4),(488-69)/4-(488/4-p1[1]-fil.shape[1]/2),(357-205)/4-(357/4-p1[0]-fil.shape[0]/2), linewidth=2, facecolor='none', edgecolor='m')
    err1 = boxErr(p1[1]-fil.shape[1]/2, p1[0]-fil.shape[0]/2, p1[1]-fil.shape[1]/2+10, p1[0]-fil.shape[0]/2,fil.shape[0],fil.shape[1])
    print("Accuracy:")
    print(err1)
    img.imshow(image)
    img.add_patch(box1)
    img.add_patch(boxt1)
    img.add_patch(box2)
    plt.show()
    
   
    
    return

## Recursive function for labeling cc
def label(mark, x, y, gray):
    mark[x, y] = count
    for xd in range(-1,2):
        for yd in range(-1,2):
            if ((xd,yd) != (0,0)):
                x2 = x + xd
                y2 = y + yd
                if (x2 >= 0 and y2 >= 0 and x2 < gray.shape[0] and y2 < gray.shape[1] and gray[x2, y2] == 255 and mark[x2, y2]==0):
                    label(mark, x2, y2, gray)

## Function to calculate moment
def moment(mat, j, k, d):
    ret = 0
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            if (mat[x][y] == d):
                ret+=(x**j)*(y**k)
    return ret
## Function to calculate centroid
def centroid(mat, d):
    x2 = moment(mat,1,0,d)/moment(mat,0,0,d)
    y2 = moment(mat,0,1,d)/moment(mat,0,0,d)
    return x2, y2
##Function to calculate central moment
def centMoment(mat, j, k, d):
    ret = 0
    x2 = moment(mat,1,0,d)/moment(mat,0,0,d)
    y2 = moment(mat,0,1,d)/moment(mat,0,0,d)
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            if (mat[x][y] == d):
                ret+=((x-x2)**j)*((y-y2)**k)
    return ret
## Function to calculate normalized central moment
def normMoment(mat, j, k, d):
    ret = 0
    x2 = moment(mat,1,0,d)/moment(mat,0,0,d)
    y2 = moment(mat,0,1,d)/moment(mat,0,0,d)
    x3 = math.sqrt(centMoment(mat,2,0,d)/moment(mat,0,0,d))
    y3 = math.sqrt(centMoment(mat,0,2,d)/moment(mat,0,0,d))
    for x in range(mat.shape[0]):
        for y in range(mat.shape[1]):
            if (mat[x][y] == d):
                ret+=(((x-x2)/x3)**j)*(((y-y2)/y3)**k)
    return ret
## Dot product helper function
def dotproduct(v1, v2):
  return sum((x*y) for x, y in zip(v1, v2))
## vector length helper
def length(v):
  return math.sqrt(dotproduct(v, v))
## Angle between two vectors function
def angle(v1, v2):
  return math.acos(dotproduct(v1, v2)/(length(v1)*length(v2)))
## Bounding box error function
def boxErr(x, y, xt, yt, dx, dy,):
    xdiff = abs(xt - x)
    ydiff = abs(yt - y)
    sum1 = xdiff*dy
    sum2 = ydiff*dx
    corner = xdiff*ydiff
    outside = 2*(sum1 + sum2 - corner)
    inside = (dx-xdiff)*(dy-ydiff)
    return inside/(outside+inside)
    

if __name__ == "__main__":
    main()