from utils import common
from utils.constant import DebugLevel
from utils.handlercv2 import HandlerCv2


class AutoGPSDestination:
    count = 0
    color_d = 20  # delta
    color_gps = (255, 237, 62)  # [255 237  62] in BGR
    color_range_lower = (color_gps[0] - color_d, color_gps[1] - color_d, color_gps[2] - color_d)
    color_range_upper = (color_gps[0] + color_d, color_gps[1] + color_d, color_gps[2] + color_d)
    cursor_loc = (260, 1230)  # Location
    map_d = 200  # delta
    map_rect = (cursor_loc[0] - map_d, cursor_loc[1] - map_d, cursor_loc[0] + map_d, cursor_loc[1] + map_d)
    running = False

    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to drive to destination
        :param hcv2:
        """
        common.debug("Create AutoGPSDestination", DebugLevel.CLASS)
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()

    def run(self):
        """
        Need to be run from game esc menu
        """
        common.debug("Start AutoGPSDestination (after 5 secs)", DebugLevel.FUNCTIONS)
        common.sleep(5)
        common.press("esc")
        common.keyDown("z", 2)
        self.count = 0
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            if not self.hcv2.check_color(self.color_range_lower, self.color_range_upper, self.map_rect):
                common.debug("Path not found: " + str(self.count), DebugLevel.INFO)
                self.count += 1
                if self.count >= 2:
                    common.debug("Stop")
                    self.running = False
            else:
                self.count = 0
            common.sleep(.25)
        common.keyDown("z")
        common.press("esc", 0)
        common.debug("Done AutoGPSDestination", DebugLevel.FUNCTIONS)
