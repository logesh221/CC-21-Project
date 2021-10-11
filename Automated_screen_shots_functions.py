import time
import cv2
import pyautogui
import os
import numpy as np
from skimage.metrics import structural_similarity


def check_img_similarity(a, b):
    """
    Returns the difference between two images
    :param a:
        image 1
    :param b:
        image 2
    :return:
         Difference between a and b
    """
    c = cv2.cvtColor(np.array(a), cv2.COLOR_BGR2GRAY)
    d = cv2.cvtColor(np.array(b), cv2.COLOR_BGR2GRAY)
    # Compute SSIM between two images
    (score, diff) = structural_similarity(c, d, full=True)
    return score


def screen_shot(name: str, time_limit: int):
    """
     Captures the screen shot and saves it to a directory

    :param name:
            The full path where a new directory is created
    :param time_limit:
            The duration during which screenshots are saved

    """

    time_start = time.time()
    time_limit = time_limit * 60

    # name = "\\".join(name.split("\\"))

    if not os.path.exists(name):  # checking for existing directory if True creates a new path
        os.mkdir(name)

    temp = pyautogui.screenshot()
    i = 0

    while True:
        my_screenshot = pyautogui.screenshot()  # captures the screen shot
        a = my_screenshot

        if check_img_similarity(a, temp) < 0.9:
            my_screenshot.save('{}\\{}.jpeg'.format(name, i))
            temp = a

        time.sleep(1)

        if time.time() - time_start > time_limit: break
        i += 1
    return 0


def time__table(table: str, full_path: str ):
    """
    Creates multiple directory and saves the jpeg with r to time table

    :param table:
        The time table
    :param full_path:
        path where the new directories to be created
    """
    the_list = [x.split(":") for x in table.split(" ")]
    for i in the_list:
        path = full_path + "//" + i[0]
        screen_shot(path, int(i[1]))
    return 0