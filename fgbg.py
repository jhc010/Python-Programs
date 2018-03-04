from scipy import misc as sp
import numpy as np
import pylab as plt
import sys

def main():
    
    ## Foreground background recognition
    if (sys.argv[1] == ""):
        gray = sp.imread('coins_pix.jpg',mode='L')
    else:
        try:
            gray = sp.imread(sys.argv[0],mode='L')
        except:
            gray = sp.imread('coins_pix.jpg',mode='L')
            
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
        
            
    plt.imshow(gray)
    plt.show()
    
if __name__ == "__main__":
    main();