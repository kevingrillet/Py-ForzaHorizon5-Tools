import time

import pyautogui

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoGPSDestination:
    delta = 20
    gps_color = (255, 237, 62)  # [255 237  62] in BGR
    map_rect = (210, 1180, 310, 1260)  # 260, 1230

    def __init__(self, cv2: HandlerCv2 = None):
        common.debug("Create AutoGPSDestination")
        if cv2:
            self.cv2 = cv2
        else:
            self.cv2 = HandlerCv2()
        self.color_range_lower = (self.gps_color[0] - self.delta,
                                  self.gps_color[1] - self.delta,
                                  self.gps_color[2] - self.delta)
        self.color_range_upper = (self.gps_color[0] + self.delta,
                                  self.gps_color[1] + self.delta,
                                  self.gps_color[2] + self.delta)
        self.running = False

    def run(self):
        common.debug("Start AutoGPSDestination")
        time.sleep(1)
        pyautogui.press('esc')
        time.sleep(2)
        pyautogui.keyDown('z')
        self.running = True
        while self.running:
            self.cv2.require_new_capture = True
            if not self.cv2.check_color(self.color_range_lower, self.color_range_upper, self.map_rect):
                self.running = False
            time.sleep(1)
        pyautogui.keyUp('z')
        pyautogui.press('esc')
        common.debug("Done AutoGPSDestination")
