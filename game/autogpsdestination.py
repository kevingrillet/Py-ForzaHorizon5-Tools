from utils import common, superdecorator
from utils.handlercv2 import HandlerCv2


@superdecorator.decorate_all_functions()
class AutoGPSDestination:
    def __init__(self, hcv2: HandlerCv2 = None):
        """
        Prepare to drive to destination
        :param hcv2:
        """
        self.hcv2 = hcv2 if hcv2 else HandlerCv2()
        color_d = 20  # delta
        color_gps = (255, 237, 62)  # [255 237  62] in BGR
        self.color_range_lower = (color_gps[0] - color_d, color_gps[1] - color_d, color_gps[2] - color_d)
        self.color_range_upper = (color_gps[0] + color_d, color_gps[1] + color_d, color_gps[2] + color_d)
        cursor_loc = (260, 1230)  # Location
        map_d = 200  # delta
        self.map_rect = (cursor_loc[0] - map_d, cursor_loc[1] - map_d, cursor_loc[0] + map_d, cursor_loc[1] + map_d)
        self.running = False

    def run(self):
        """
        Need to be run from game esc menu
        """
        common.sleep(5, 'Waiting 5 secs, please focus Forza Horizon 5.')
        common.moveTo((10, 10))
        common.press('esc')
        common.keyDown('z', 2)
        count = 0
        self.running = True
        while self.running:
            self.hcv2.require_new_capture = True
            if not self.hcv2.check_color(self.color_range_lower, self.color_range_upper, self.map_rect):
                common.info('Path not found: ' + str(count))
                count += 1
                if count >= 2:
                    common.debug('Stop')
                    self.running = False
            else:
                count = 0
            common.sleep(.25)
        common.keyDown('z')
        common.press('esc', 0)
