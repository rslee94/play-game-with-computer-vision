import cv2  # https://docs.opencv.org/4.x/
import numpy as np
import pyautogui
import mss  # https://python-mss.readthedocs.io/index.html
from time import sleep

pyautogui.FAILSAFE = False

sct = mss.mss()
default_monitor = sct.monitors[
    1
]  # https://python-mss.readthedocs.io/api.html#mss.tools.mss.base.MSSBase.monitors

def click_element(xy):
    xy_l = xy.split()
    click_x = xy_l[0]
    click_y = xy_l[1]

    pyautogui.clikc(x=click_x, y=click_y)

def detect_element(image):
    detected = False
    detected_element = None
    while True:
        for i in image_list:
        #image finding algo
        detected = True
        detected_element = image[i]
        detected_element_coord = 
        break
    result_string = None
    if detected == True:
        r1 = "T"
    else:
        r1 = "false"

    if detected_element != None:
        r2 = detected_element


    rfinal = r1+","+r2
    return rfinal
    #123,456
relic = image_path(relic.png)

def detect_and_click(image_path):
    element = detect_element(image_path)
    click_element(element)



relic_element = detect_element(relic)
click_element(relic_element)
return_element = detect_element(back)
click_element(return_element)

click_element(123,456)

def click_template_image(
    template_image_path: str,
    monitor=default_monitor,
    threshold: float = 0.7,
    number_of_clicks: int = 1,
):
    print(f"{template_image_path} search")
    template_image = cv2.imread(template_image_path, 1)

    # Screenshot
    # game_screenshot_path = "sct_{width}x{height}.png".format(**monitor)
    # sct_img = sct.grab((0, 0, monitor["width"], monitor["height"]))
    # mss.tools.to_png(sct_img.rgb, sct_img.size, output=game_screenshot_path)  # type:ignore
    # game_screenshot = cv2.imread(game_screenshot_path, 1)
    game_screenshot = np.array(sct.grab((0, 0, monitor["width"], monitor["height"])))
    game_screenshot = game_screenshot[:, :, :3]  # remove alpha

    # https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
    search_result = cv2.matchTemplate(
        game_screenshot, template_image, cv2.TM_CCOEFF_NORMED
    )

    # View Result
    # cv2.imshow('Result', result)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # Get Max Result
    # print(cv2.minMaxLoc(result))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(search_result)
    print(max_val)

    # print(np.where(result >= threshold))
    y_coords, x_coords = np.where(search_result >= threshold)  # type:ignore
    # the screenshot might have a different resolution/dimensions form the actual screen. 
    # the width & height reset multipliers are used to reset the w & h (screenshot's dimensions) to the actual screen's dimensions 
    width_reset_multiplier = game_screenshot.shape[1] / monitor["width"]
    height_reset_multiplier = game_screenshot.shape[0] / monitor["height"]
    w = template_image.shape[1]
    h = template_image.shape[0]
    for idx in range(number_of_clicks):
        if idx + 1 > len(x_coords):
            continue

        x, y = x_coords[idx], y_coords[idx]

        x /= width_reset_multiplier
        y /= height_reset_multiplier

        # print(x,y)

        x_c = int((x + x + w) // 2)
        y_c = int((y + y + h) // 2)

        pyautogui.click(x=x_c, y=y_c)  # type:ignore

        sleep(0.3) # wait for popups to appear

        # Draw circles on points found
        # cv2.circle(game_screenshot, (x, y), 10, (255, 0, 0), 2)

    # cv2.imwrite('./GameScreenshot.png', game_screenshot)

    # cv2.imshow('Game screenshot', game_screenshot)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # cv2.imwrite('./GameScreenshot.png', game_screenshot)


close_buttons = [
    "close.png",
    "close_big.png",
    "continue_level.png",
    "yes_close_offer.png",
]

valuables = [
    "cash.png",
    "star.png",
    "key.png",
    "relic_1.png",
    "free_2.png",
    "free_1.png",
]

return_buttons = [
    "return.png",
]

while True:

    for valuable_image in valuables:
        click_template_image("images/" + valuable_image)

        for close_button_image in close_buttons:
            click_template_image("images/" + close_button_image)

            for return_button_image in return_buttons:
                click_template_image("images/" + return_button_image)


while True:
    capture_monitor()
    element_sequence() #order: find resoure > collect resource > exit to main
        detect_button()
        click_button()

