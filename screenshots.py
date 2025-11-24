import cv2 as cv
import numpy as np
import win32gui, win32con, win32ui
from time import sleep

#get screenshot from screen region
def screenshot():
    w = 1440
    h = 810
    
    hwnd = win32gui.FindWindow(None, ' ')

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (240, 135), win32con.SRCCOPY)

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (h,w,4)


    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    img = img[...,:3]
    img = np.array(img)
    return img

path = ""
x = 0
while True:
    #Save image every 3 seconds
    cv.imwrite(path+str(x)+".jpg", screenshot())
    print(x)
    sleep(3)
    x+=1