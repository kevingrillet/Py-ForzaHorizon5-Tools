import numpy as np
import win32gui, win32ui, win32con, win32api


class HandlerWin32:
    width = height = left = top = 0
    hwin = region = None

    def __init__(self, window_name: str = None, fullscreen: bool = True, sos: bool = False,
                 region: (int, int, int, int) = None):
        """
        Prepare for capture
        :param window_name: Name of window
        :param fullscreen: Is it in fullscreen?
        :param sos: Help if capture is black (instead of using window handler)
        :param region:
        """
        self.sos = sos
        if window_name:
            self.hwin = win32gui.FindWindow(None, window_name)
            if not self.hwin:
                raise Exception('Window not found: {}'.format(window_name))
            self.fullscreen = fullscreen
            region = win32gui.GetWindowRect(self.hwin)
            if sos:
                self.hwin = win32gui.GetDesktopWindow()
        else:
            self.hwin = win32gui.GetDesktopWindow()
        self.set_region(region)

    def screenshot(self):
        """
        Take a screenshot of region / hwin
        :return: image: ndarray
        """
        hwindc = win32gui.GetWindowDC(self.hwin)
        srcdc = win32ui.CreateDCFromHandle(hwindc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, self.width, self.height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (self.width, self.height), srcdc, (self.left, self.top), win32con.SRCCOPY)

        signedIntsArray = bmp.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(self.hwin, hwindc)
        win32gui.DeleteObject(bmp.GetHandle())

        img = img[..., :3]
        img = np.ascontiguousarray(img)

        return img

    def set_region(self, region: (int, int, int, int) = None):
        """
        Define the capture region
        :param region: rect
        """
        self.region = region

        if self.region:
            if self.hwin or self.sos:
                self.width = self.region[2] - self.region[0]
                self.height = self.region[3] - self.region[1]
                if self.fullscreen:
                    self.left = 0
                    self.top = 0
                else:
                    border_pixels = 8
                    titlebar_pixels = 30
                    self.width = self.width - (border_pixels * 2)
                    self.height = self.height - titlebar_pixels - border_pixels
                    self.left = border_pixels
                    self.top = titlebar_pixels

            else:
                self.left, self.top, x2, y2 = self.region
                self.width = x2 - self.left + 1
                self.height = y2 - self.top + 1
        else:
            self.width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
            self.height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
            self.left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
            self.top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)
