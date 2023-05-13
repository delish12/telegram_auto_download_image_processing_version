import pyautogui as pg
import numpy as np
import time
import cv2


no_of_eps = int(input('enter no of episodes='))
time.sleep(5)
# wait for download variable
wfd = True
#time to wait between each download
delay = 2

for i in range(no_of_eps):
    sc = pg.screenshot()
    sc = cv2.cvtColor(np.array(sc),cv2.COLOR_RGB2BGR)
    coordlist = list(pg.locateAllOnScreen('download.png'))
    listlen = len(coordlist)
    now = coordlist[0]
    x = (now.left + now.left+now.width) // 2
    y = (now.top + now.top+now.height) // 2
    pg.click(x = x,y = y)
    if listlen < 2:
        while(pg.locateOnScreen('open.png')):
            pg.scroll(-100)
    if wfd:
        while(True):
            time.sleep(delay)
            if not pg.locateOnScreen('cancel.png'):
                break
    else:
        time.sleep(delay)
