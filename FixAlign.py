from scipy import misc as sp
import numpy as np
import pylab as plt
from matplotlib import patches
import math
import sys

count = 0
## Finding the central moment of an object and fix its rotation
def main():
    global count
    if (sys.argv[1] == ""):
        pic = 'pen.jpg'
    else:
        try:
            gray = sp.imread(sys.argv[0],mode='L')
            pic = sys.argv[0]
        except:
            pic = 'pen.jpg'
    
    gray = sp.imread(pic,mode='L')
    gray = sp.imresize(gray,0.25)
    
    plt.imshow(gray)
    plt.show()
    
    hist = np.histogram(gray, range=(0,255), bins=255)
    pix = 0
    valSum = 0
    valTotal = 0
    thresh = 0
    maxThresh = 0
    maxThreshIdx = 0
    totalPix = gray.shape[0]*gray.shape[1]
    vals = hist[0]
    
    for idx, i in enumerate(hist[0]):
        valTotal += idx*vals[idx]
    
    for idx, i in enumerate(hist[0]):
        pix += vals[idx]
        pixLeft = totalPix - pix
        if (pix == 0): continue
        if (pixLeft == 0): break
        valSum += idx*vals[idx]
        m0 = valSum/pix
        m1 = (valTotal - valSum)/pixLeft
        thresh = pix*pixLeft*(m0-m1)*(m0-m1)
        if (thresh > maxThresh):
            maxThresh = thresh
            maxThreshIdx = idx

    
    for x in range(gray.shape[0]):
        for y in range(gray.shape[1]):
            if (gray[x][y] > maxThreshIdx):
                gray[x][y] = 255
            else:
                gray[x][y] = 0
                
    ret2 = sp.imread(pic, mode="RGB")
    mark = sp.imread(pic,mode = 'L')
    
    mark = sp.imresize(mark,0.25)
    ret2 = sp.imresize(ret2,0.25)
    
    mark.fill(0)
    for x in range(mark.shape[0]):
        for y in range(mark.shape[1]):
            if (gray[x][y] == 255 and mark[x][y] == 0):
                count += 1
                label(mark, x, y, gray)

    for x in range(mark.shape[0]):
        for y in range(mark.shape[1]):
            if (mark[x][y] == 1):
                ret2[x][y] = [255, 0, 0]
            if (mark[x][y] == 2):
                ret2[x][y] = [0, 255, 0]
            if (mark[x][y] == 3):
                ret2[x][y] = [0, 0, 255]
            if (mark[x][y] == 4):
                ret2[x][y] = [255, 255, 0]
            if (mark[x][y] == 5):
                ret2[x][y] = [0, 255, 255]
            if (mark[x][y] == 0):
                ret2[x][y] = [0, 0, 0]
    count = 0
    
    plt.imshow(ret2)
    plt.show()
    
    mark2 = np.copy(mark)
    
    fig,img = plt.subplots(1)
    x,y = centroid(mark, 1)
    val1 = centMoment(mark, 2, 0, 1)
    val2 = centMoment(mark, 1, 1, 1)
    val3 = centMoment(mark, 1, 1, 1)
    val4 = centMoment(mark, 0, 2, 1)
    scmm = np.matrix([[val1,val2], [val3,val4]])
    eigenvals, eigenvecs = np.linalg.eig(scmm)
    arrow1 = patches.Arrow(x,y,20*eigenvecs[0,0],20*eigenvecs[0,1], color='green', lw=4.0)
    arrow2 = patches.Arrow(x,y,20*eigenvecs[1,0],20*eigenvecs[1,1], color='blue', lw=4.0)
    img.imshow(ret2)
    img.add_patch(arrow2)
    img.add_patch(arrow1)
    plt.show()
    theta = angle([1,0], [eigenvecs[1,0],eigenvecs[1,1]])
    theta = theta
    R = np.matrix([[math.cos(theta),-math.sin(theta)],[math.sin(theta), math.cos(theta)]])
    cent = np.matrix([[x],[y]])
    
    #Rotate
    for x2 in range(ret2.shape[0]):
        for y2 in range(ret2.shape[1]):
            p = np.matrix([[x2],[y2]])
            p2 = R*(p-cent)+cent
            if (int(p2[0]) < mark.shape[0] and int(p2[0]) >= 0 and int(p2[1]) < mark.shape[1] and int(p2[1]) >= 0):
                mark2[int(p2[0])][int(p2[1])] = mark[x2][y2]
    # Fix Rotate            
    for x2 in range(ret2.shape[0]):
        for y2 in range(ret2.shape[1]):
            p = np.matrix([[x2],[y2]])
            p2 = R*(p-cent)+cent
            p2[0] -= 1
            p2[1] -= 1
            if (int(p2[0]) < mark.shape[0] and int(p2[0]) >= 0 and int(p2[1]) < mark.shape[1] and int(p2[1]) >= 0):
                mark2[int(p2[0])][int(p2[1])] = mark[x2][y2]
    
    #Display with color
    for x in range(mark.shape[0]):
        for y in range(mark.shape[1]):
            if (mark2[x][y] == 1):
                ret2[x][y] = [255, 0, 0]
            if (mark2[x][y] == 2):
                ret2[x][y] = [0, 255, 0]
            if (mark2[x][y] == 3):
                ret2[x][y] = [0, 0, 255]
            if (mark2[x][y] == 4):
                ret2[x][y] = [255, 255, 0]
            if (mark2[x][y] == 5):
                ret2[x][y] = [0, 255, 255]
            if (mark2[x][y] == 0):
                ret2[x][y] = [0, 0, 0]
    
    fig,img = plt.subplots(1)
    x,y = centroid(mark2, 1)
    val1 = centMoment(mark2, 2, 0, 1)
    val2 = centMoment(mark2, 1, 1, 1)
    val3 = centMoment(mark2, 1, 1, 1)
    val4 = centMoment(mark2, 0, 2, 1)
    scmm = np.matrix([[val1,val2], [val3,val4]])
    eigenvals, eigenvecs = np.linalg.eig(scmm)
    arrow1 = patches.Arrow(x,y,20*eigenvecs[0,0],20*eigenvecs[0,1], color='green', lw=4.0)
    arrow2 = patches.Arrow(x,y,20*eigenvecs[1,0],20*eigenvecs[1,1], color='blue', lw=4.0)
    img.imshow(ret2)
    img.add_patch(arrow2)
    img.add_patch(arrow1)        
    plt.show()


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
    main();