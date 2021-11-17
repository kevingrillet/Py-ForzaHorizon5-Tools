import time

import pyautogui

from utils import common
from utils.handlercv2 import HandlerCv2


class AutoGPSDestination:
    count = 0
    delta = 20
    gps_color = (255, 237, 62)  # [255 237  62] in BGR
    cursor_location = (260, 1230)
    map_delta = 75
    map_rect = (cursor_location[0] - map_delta, cursor_location[1] - map_delta,
                cursor_location[0] + map_delta, cursor_location[1] + map_delta)

    def __init__(self, cv2: HandlerCv2 = None):
        common.debug("Create AutoGPSDestination")
        if cv2:
            self.hcv2 = cv2
        else:
            self.hcv2 = HandlerCv2()
        self.color_range_lower = (self.gps_color[0] - self.delta,
                                  self.gps_color[1] - self.delta,
                                  self.gps_color[2] - self.delta)
        self.color_range_upper = (self.gps_color[0] + self.delta,
                                  self.gps_color[1] + self.delta,
                                  self.gps_color[2] + self.delta)
        self.running = False

    def run(self):
        common.debug("Start AutoGPSDestination (after 2 secs)")
        time.sleep(2)
        pyautogui.press('esc')
        time.sleep(.5)
        pyautogui.keyDown('z')
        time.sleep(.5)
        self.count = 0
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            if not self.hcv2.check_color(self.color_range_lower, self.color_range_upper, self.map_rect):
                common.debug("Path not found: " + str(self.count))
                self.count += 1
                if self.count >= 2:
                    common.debug("Stop")
                    self.running = False
            else:
                self.count = 0
            time.sleep(.25)
        pyautogui.keyUp('z')
        pyautogui.press('esc')
        common.debug("Done AutoGPSDestination")
