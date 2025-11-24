import cv2
from ultralytics import YOLO
import cv2 as cv
import numpy as np
import win32gui, win32con, win32ui

SHOW_CLASS = [True,   # 0 Titanium
            True,   # 1 Silicon
            True,   # 2 Magnesium
            True,   # 3 Cobalt
            True,   # 4 Ice
            True,   # 5 Aluminium
            True,   # 6 Uranium
            True,   # 7 Osmium
            True,   # 8 Sulfur
            True,   # 9 Zeolite
            True,   # 10 Iridium
            True    # 11 Iron
              ]
SCALE = 0.4


def screenshot(): #Screen aufnehmen
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

model = YOLO("detector.pt") #Modell laden

while True:
    screen = screenshot()
    sh, sw = screen.shape[:2]
    small = cv2.resize(screen, (int(sw * SCALE), int(sh * SCALE)), interpolation=cv2.INTER_LINEAR)

    results = model.predict( #model prediction
        source=small,
        conf=0.5,
        iou=0.55,
        verbose=False
    )

    results = results[0]
    boxes = results.boxes #prediction data
    names = model.names

    for b in boxes:
        cls_id = int(b.cls[0].item())
        if not SHOW_CLASS[cls_id]:
            continue
        score = float(b.conf[0].item())
        x1, y1, x2, y2 = b.xyxy[0].tolist()
        x1 = int(x1 / SCALE)
        y1 = int(y1 / SCALE)
        x2 = int(x2 / SCALE)
        y2 = int(y2 / SCALE)

        label = f"{names[cls_id]} {score:.2f}"
        cv.rectangle(screen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv.putText(screen, label, (x1, max(y1 - 5, 15)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
        
    cv.imshow('Prediction', screen)
    cv.waitKey(1)
