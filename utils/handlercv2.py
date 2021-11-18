import random
from datetime import datetime

import cv2

from utils import constant
from utils.handlerwin32 import HandlerWin32
from utils.common import debug, fps


class HandlerCv2:
    def __init__(self):
        self.find_start = None
        self.find_end = None
        self.image_read_flag = cv2.IMREAD_COLOR
        self.method = cv2.TM_CCOEFF_NORMED
        self.require_new_capture = True
        self.show_debug_image = False
        self.target_image = None
        self.target_image_debug = None
        self.threshold = 0.9
        self.hwin32 = HandlerWin32(window_name=constant.WINDOW_NAME, fullscreen=True, sos=True)

    def check_color(self, crl: (int, int, int) = None, cru: (int, int, int) = None,
                    rect: (int, int, int, int) = None) -> bool:
        """
            Take capture & check if image match
        :param crl: color_range_lower (B,G,R)
        :param cru: color_range_upper (B,G,R)
        :param rect: rect
        """
        self.get_image()
        for x in range(rect[0], rect[2]):
            for y in range(rect[1], rect[3]):
                c = self.target_image[y, x]
                if crl[0] < c[0] < cru[0] and crl[1] < c[1] < cru[1] and crl[2] < c[2] < cru[2]:
                    return True
        return False

    def check_match(self, data_image) -> bool:
        """
            Take capture & check if image match
            coordinates can be accessed with find_start / find_end or directly tap with tap_find
        :param data_image: Image to find
        :return: true / false
        """

        self.get_image()
        return self.match(data_image)

    def dev(self):
        """
            Run dev mode, showing the capture
        """
        debug("dev > s to save, q to quit")
        while True:
            self.get_image(True)
            cv2.namedWindow("dev", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("dev", 1600, 900)
            cv2.imshow("dev", self.target_image)  # Show image in window
            debug(str(fps()))  # Print FPS (crappy rate yeah)
            k = cv2.waitKey(25)  # Get key pressed every 25ms
            if k == ord("s"):  # If "s" is pressed
                # Save the image in .temp/
                cv2.imwrite(".temp/" + str(datetime.now()).replace(":", ".") + ".jpg", self.target_image)
            elif k == ord("q"):  # If "q" is pressed
                cv2.destroyWindow("dev")  # Destroy the window
                break

    def draw_debug(self):
        """
            Draw rect on find & show
        """
        self.target_image_debug = cv2.rectangle(self.target_image_debug, self.find_start, self.find_end, (0, 255, 0), 5)
        self.show_image()

    def get_image(self, force: bool = False):
        """
            take capture & show
        :param force: force capture, else use require_new_capture
        """
        if self.require_new_capture or force:
            self.require_new_capture = False
            self.target_image_debug = self.target_image = self.hwin32.screenshot()
            self.show_image()

    def load_images(self, images_list: list[str] = None) -> dict:
        """
            Load images and return dictionary
        :param images_list: [path_to_image, ...]
        :return: dict[path]={image, h, w}
        """
        if images_list is None:
            images_list = []
        res = {}
        for image in images_list:
            # global_utils.debug("load_images > " + image, -1)
            img = cv2.imread("./images/" + constant.LANG.value + "/" + image + ".jpg", self.image_read_flag)
            if img is not None:
                h, w = img.shape[:2]
                res[image] = (img, h, w)
        return res

    def match_template(self, find_image) -> bool:
        """
            return true if image match
        :param find_image: Image to find
        :return: true / false
        """
        return cv2.matchTemplate(self.target_image, find_image, self.method)

    def match(self, data_image) -> bool:
        """
            return true if image match & set find_start & find_end
        :param data_image: Image to find
        :return: true / false
        """
        find_image, h, w = data_image
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(self.match_template(find_image))
        if max_val < self.threshold:
            self.find_start = None
            self.find_end = None
            return False
        self.find_start = max_loc
        self.find_end = (int(max_loc[0] + w), int(max_loc[1] + h))
        self.draw_debug()
        return True

    def random_find(self) -> (int, int):
        """
            return random coords (x,y) between find_start & find_end
        """
        x1, y1 = self.find_start
        x2, y2 = self.find_end
        return random.randint(x1, x2), random.randint(y1, y2)

    def show_image(self, image=None):
        """
            show image if show_debug_image is set to True
        :param image: Image to show
        """
        if not self.show_debug_image:
            return
        if image is None:
            image = self.target_image_debug
        cv2.namedWindow("show_image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("show_image", 1600, 900)
        cv2.imshow("show_image", image)
        k = cv2.waitKey(0)
        if k == ord("s"):
            cv2.imwrite(".temp/" + str(datetime.now()).replace(":", ".") + ".jpg", self.target_image)
        cv2.destroyWindow("show_image")
