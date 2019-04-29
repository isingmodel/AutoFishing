import copy
import platform
import random
import sys
import time
import time

import mss
import mss.tools
import numpy as np
import pyautogui
import win32con
from win32api import GetSystemMetrics

if platform.system() != "Windows":
    print("only available on Windows")

else:
    scale_factor = 1440. / GetSystemMetrics(1)

    pyautogui.FAILSAFE = False
    monitor = {"top": int(640 / scale_factor),
               "left": int(1279 / scale_factor),
               "width": int(2),
               "height": int(10 / scale_factor)}

    time.sleep(5)

    # initializing parameters
    caught = 0
    pyautogui.press('w')
    time0 = time.time()
    counter = 0
    counter2 = 0
    time2 = time.time()
    tongbal = False
    stack = 0
    caught_count = 12

    monitor_tongbal = {"top": int(10 / scale_factor),
                       "left": int(378 / scale_factor),
                       "width": int(2 / scale_factor),
                       "height": int(2 / scale_factor)}

    while True:
        counter += 1
        if time.time() - time0 > 2.5:
            with mss.mss() as sct:
                img = np.array(sct.grab(monitor))
                c1 = np.average([img[2][1][0], img[3][1][0], img[4][1][0]]) - 110
                c2 = np.average([img[2][1][1], img[3][1][1], img[4][1][1]]) - 200
                c3 = np.average([img[2][1][2], img[3][1][2], img[4][1][2]]) - 220
                # diff = c1 + c2 + c3
                if (c1 > 0 and c2 > 0 and c3 > 0 and c1 < 90) or c3 == 25:
                    print(c1, c2, c3)
                    caught = 1

                # diff_backup = copy.deepcopy(diff)

        # gotcha
        if caught:
            ### end up fishing
            print("gacha")
            pyautogui.press('w')
            time.sleep(6.6 + random.random() / 5)

            ### tongbal skill in         
            with mss.mss() as sct:
                sct_img = np.array(sct.grab(monitor_tongbal))

            if sct_img[0][0][0] < 100 and sct_img[0][0][1] < 100 and tongbal is False:
                pyautogui.moveTo(980 / scale_factor + random.random() * 5,
                                 790 / scale_factor + random.random() * 5)
                time.sleep(0.3)
                pyautogui.click(button='right')
                time.sleep(0.5)
                print("tongbal intput")
                pyautogui.press('g')
                tongbal = False
                time2 = time.time()
                time.sleep(5.2)
                # move back
                pyautogui.moveTo(1500 / scale_factor + random.random() * 5,
                                 590 / scale_factor)
                time.sleep(0.5)
                pyautogui.click(button='right')
                tongbal = True
                time.sleep(1.5)

            ### tongbal skill out
            if time.time() - time2 > 303:
                pyautogui.moveTo(980 / scale_factor + random.random() * 5,
                                 790 / scale_factor + random.random() * 5)
                time.sleep(0.3)
                pyautogui.click(button='right')
                time.sleep(0.5)
                print("tongbal output")
                pyautogui.press('g')
                time2 = time.time()
                time.sleep(5.2)
                # move back
                pyautogui.moveTo(1500 / scale_factor + random.random() * 5,
                                 590 / scale_factor)
                time.sleep(0.5)
                pyautogui.click(button='right')
                tongbal = False
                time.sleep(1.5)
            else:
                time.sleep(4)

            ### some movings
            lala = random.random()
            if lala < 0.33:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 700 / scale_factor)
            elif lala < 0.67:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 710 / scale_factor + random.random() * 5)
            else:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 700 / scale_factor + random.random() * 5)
            pyautogui.click(button='right')
            time.sleep(random.random() / 5.)

            # next fishing
            pyautogui.press('w')
            time.sleep(random.random() / 5.)

            pyautogui.moveTo(1785 / scale_factor + random.random(), 615 / scale_factor + random.random())

            caught = 0
            counter2 = + 1
            time0 = time.time()
            caught_count = 20

        # fail!!
        if time.time() - time0 > 27:
            print("fail")
            lala = random.random()
            if lala < 0.33:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 700 / scale_factor + random.random() * 5)
            elif lala < 0.67:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 710 / scale_factor)
            else:
                pyautogui.moveTo(1780 / scale_factor + random.random() * 5,
                                 700 / scale_factor + random.random() * 5)
            time.sleep(0.1)
            pyautogui.click(button='right')
            time.sleep(0.2)
            pyautogui.press('w')
            caught = 0
            time0 = time.time()

        else:
            if caught_count > 1:
                counter -= 1
                caught_count -= 1
                pass
            else:
                if counter % 200 == 199:
                    pyautogui.moveTo(1400 / scale_factor + random.random() * 20,
                                     720 / scale_factor + random.random() * 20)
                    pyautogui.click(button='right')
                    time.sleep(0.1)
                    pyautogui.press('enter')
                    print("enter")
        time.sleep(0.12)
