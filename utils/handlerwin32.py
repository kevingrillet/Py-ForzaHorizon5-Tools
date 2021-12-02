import ctypes
import time

import numpy as np
import win32api
import win32con
import win32gui
import win32ui


class HandlerWin32:
    width = height = left = top = 0
    hwin = region = None

    def __init__(self, window_name: str = None, fullscreen: bool = True, sos: bool = False,
                 region: (int, int, int, int) = None):
        """
        Prepare for capture
        :param window_name: Name of window
        :param fullscreen: Is it in fullscreen
        :param sos: Help if capture is black instead of using window handler
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

    @staticmethod
    def get_keyboard_language() -> str:
        # https://stackoverflow.com/a/66756115
        """
        Gets the keyboard language in use by the current
        active window process.
        """

        languages = {'0x436': 'Afrikaans - South Africa', '0x041c': 'Albanian - Albania',
                     '0x045e': 'Amharic - Ethiopia', '0x401': 'Arabic - Saudi Arabia', '0x1401': 'Arabic - Algeria',
                     '0x3c01': 'Arabic - Bahrain', '0x0c01': 'Arabic - Egypt', '0x801': 'Arabic - Iraq',
                     '0x2c01': 'Arabic - Jordan', '0x3401': 'Arabic - Kuwait', '0x3001': 'Arabic - Lebanon',
                     '0x1001': 'Arabic - Libya', '0x1801': 'Arabic - Morocco', '0x2001': 'Arabic - Oman',
                     '0x4001': 'Arabic - Qatar', '0x2801': 'Arabic - Syria', '0x1c01': 'Arabic - Tunisia',
                     '0x3801': 'Arabic - U.A.E.', '0x2401': 'Arabic - Yemen', '0x042b': 'Armenian - Armenia',
                     '0x044d': 'Assamese', '0x082c': 'Azeri (Cyrillic)', '0x042c': 'Azeri (Latin)', '0x042d': 'Basque',
                     '0x423': 'Belarusian', '0x445': 'Bengali (India)', '0x845': 'Bengali (Bangladesh)',
                     '0x141A': 'Bosnian (Bosnia/Herzegovina)', '0x402': 'Bulgarian', '0x455': 'Burmese',
                     '0x403': 'Catalan', '0x045c': 'Cherokee - United States',
                     '0x804': "Chinese - People's Republic of China", '0x1004': 'Chinese - Singapore',
                     '0x404': 'Chinese - Taiwan', '0x0c04': 'Chinese - Hong Kong SAR', '0x1404': 'Chinese - Macao SAR',
                     '0x041a': 'Croatian', '0x101a': 'Croatian (Bosnia/Herzegovina)', '0x405': 'Czech',
                     '0x406': 'Danish', '0x465': 'Divehi', '0x413': 'Dutch - Netherlands', '0x813': 'Dutch - Belgium',
                     '0x466': 'Edo', '0x409': 'English - United States', '0x809': 'English - United Kingdom',
                     '0x0c09': 'English - Australia', '0x2809': 'English - Belize', '0x1009': 'English - Canada',
                     '0x2409': 'English - Caribbean', '0x3c09': 'English - Hong Kong SAR', '0x4009': 'English - India',
                     '0x3809': 'English - Indonesia', '0x1809': 'English - Ireland', '0x2009': 'English - Jamaica',
                     '0x4409': 'English - Malaysia', '0x1409': 'English - New Zealand',
                     '0x3409': 'English - Philippines', '0x4809': 'English - Singapore',
                     '0x1c09': 'English - South Africa', '0x2c09': 'English - Trinidad', '0x3009': 'English - Zimbabwe',
                     '0x425': 'Estonian', '0x438': 'Faroese', '0x429': 'Farsi', '0x464': 'Filipino',
                     '0x040b': 'Finnish', '0x040c': 'French - France', '0x080c': 'French - Belgium',
                     '0x2c0c': 'French - Cameroon', '0x0c0c': 'French - Canada',
                     '0x240c': 'French - Democratic Rep. of Congo', '0x300c': "French - Cote d'Ivoire",
                     '0x3c0c': 'French - Haiti', '0x140c': 'French - Luxembourg', '0x340c': 'French - Mali',
                     '0x180c': 'French - Monaco', '0x380c': 'French - Morocco', '0xe40c': 'French - North Africa',
                     '0x200c': 'French - Reunion', '0x280c': 'French - Senegal', '0x100c': 'French - Switzerland',
                     '0x1c0c': 'French - West Indies', '0x462': 'Frisian - Netherlands', '0x467': 'Fulfulde - Nigeria',
                     '0x042f': 'FYRO Macedonian', '0x083c': 'Gaelic (Ireland)', '0x043c': 'Gaelic (Scotland)',
                     '0x456': 'Galician', '0x437': 'Georgian', '0x407': 'German - Germany',
                     '0x0c07': 'German - Austria', '0x1407': 'German - Liechtenstein', '0x1007': 'German - Luxembourg',
                     '0x807': 'German - Switzerland', '0x408': 'Greek', '0x474': 'Guarani - Paraguay',
                     '0x447': 'Gujarati', '0x468': 'Hausa - Nigeria', '0x475': 'Hawaiian - United States',
                     '0x040d': 'Hebrew', '0x439': 'Hindi', '0x040e': 'Hungarian', '0x469': 'Ibibio - Nigeria',
                     '0x040f': 'Icelandic', '0x470': 'Igbo - Nigeria', '0x421': 'Indonesian', '0x045d': 'Inuktitut',
                     '0x410': 'Italian - Italy', '0x810': 'Italian - Switzerland', '0x411': 'Japanese',
                     '0x044b': 'Kannada', '0x471': 'Kanuri - Nigeria', '0x860': 'Kashmiri',
                     '0x460': 'Kashmiri (Arabic)', '0x043f': 'Kazakh', '0x453': 'Khmer', '0x457': 'Konkani',
                     '0x412': 'Korean', '0x440': 'Kyrgyz (Cyrillic)', '0x454': 'Lao', '0x476': 'Latin',
                     '0x426': 'Latvian', '0x427': 'Lithuanian', '0x043e': 'Malay - Malaysia',
                     '0x083e': 'Malay - Brunei Darussalam', '0x044c': 'Malayalam', '0x043a': 'Maltese',
                     '0x458': 'Manipuri', '0x481': 'Maori - New Zealand', '0x044e': 'Marathi',
                     '0x450': 'Mongolian (Cyrillic)', '0x850': 'Mongolian (Mongolian)', '0x461': 'Nepali',
                     '0x861': 'Nepali - India', '0x414': 'Norwegian (Bokmål)', '0x814': 'Norwegian (Nynorsk)',
                     '0x448': 'Oriya', '0x472': 'Oromo', '0x479': 'Papiamentu', '0x463': 'Pashto', '0x415': 'Polish',
                     '0x416': 'Portuguese - Brazil', '0x816': 'Portuguese - Portugal', '0x446': 'Punjabi',
                     '0x846': 'Punjabi (Pakistan)', '0x046B': 'Quecha - Bolivia', '0x086B': 'Quecha - Ecuador',
                     '0x0C6B': 'Quecha - Peru', '0x417': 'Rhaeto-Romanic', '0x418': 'Romanian',
                     '0x818': 'Romanian - Moldava', '0x419': 'Russian', '0x819': 'Russian - Moldava',
                     '0x043b': 'Sami (Lappish)', '0x044f': 'Sanskrit', '0x046c': 'Sepedi',
                     '0x0c1a': 'Serbian (Cyrillic)', '0x081a': 'Serbian (Latin)', '0x459': 'Sindhi - India',
                     '0x859': 'Sindhi - Pakistan', '0x045b': 'Sinhalese - Sri Lanka', '0x041b': 'Slovak',
                     '0x424': 'Slovenian', '0x477': 'Somali', '0x042e': 'Sorbian',
                     '0x0c0a': 'Spanish - Spain (Modern Sort)', '0x040a': 'Spanish - Spain (Traditional Sort)',
                     '0x2c0a': 'Spanish - Argentina', '0x400a': 'Spanish - Bolivia', '0x340a': 'Spanish - Chile',
                     '0x240a': 'Spanish - Colombia', '0x140a': 'Spanish - Costa Rica',
                     '0x1c0a': 'Spanish - Dominican Republic', '0x300a': 'Spanish - Ecuador',
                     '0x440a': 'Spanish - El Salvador', '0x100a': 'Spanish - Guatemala', '0x480a': 'Spanish - Honduras',
                     '0xe40a': 'Spanish - Latin America', '0x080a': 'Spanish - Mexico', '0x4c0a': 'Spanish - Nicaragua',
                     '0x180a': 'Spanish - Panama', '0x3c0a': 'Spanish - Paraguay', '0x280a': 'Spanish - Peru',
                     '0x500a': 'Spanish - Puerto Rico', '0x540a': 'Spanish - United States',
                     '0x380a': 'Spanish - Uruguay', '0x200a': 'Spanish - Venezuela', '0x430': 'Sutu',
                     '0x441': 'Swahili', '0x041d': 'Swedish', '0x081d': 'Swedish - Finland', '0x045a': 'Syriac',
                     '0x428': 'Tajik', '0x045f': 'Tamazight (Arabic)', '0x085f': 'Tamazight (Latin)', '0x449': 'Tamil',
                     '0x444': 'Tatar', '0x044a': 'Telugu', '0x041e': 'Thai', '0x851': 'Tibetan - Bhutan',
                     '0x451': "Tibetan - People's Republic of China", '0x873': 'Tigrigna - Eritrea',
                     '0x473': 'Tigrigna - Ethiopia', '0x431': 'Tsonga', '0x432': 'Tswana', '0x041f': 'Turkish',
                     '0x442': 'Turkmen', '0x480': 'Uighur - China', '0x422': 'Ukrainian', '0x420': 'Urdu',
                     '0x820': 'Urdu - India', '0x843': 'Uzbek (Cyrillic)', '0x443': 'Uzbek (Latin)', '0x433': 'Venda',
                     '0x042a': 'Vietnamese', '0x452': 'Welsh', '0x434': 'Xhosa', '0x478': 'Yi', '0x043d': 'Yiddish',
                     '0x046a': 'Yoruba', '0x435': 'Zulu', '0x04ff': 'HID (Human Interface Device)'}

        user32 = ctypes.WinDLL('user32', use_last_error=True)

        # Get the current active window handle
        handle = user32.GetForegroundWindow()

        # Get the thread id from that window handle
        threadid = user32.GetWindowThreadProcessId(handle, 0)

        # Get the keyboard layout id from the threadid
        layout_id = user32.GetKeyboardLayout(threadid)

        # Extract the keyboard language id from the keyboard layout id
        language_id = layout_id & (2 ** 16 - 1)

        # Convert the keyboard language id from decimal to hexadecimal
        language_id_hex = "0x{:04x}".format(int(hex(language_id), 16))

        # Check if the hex value is in the dictionary.
        if language_id_hex in languages.keys():
            return languages[language_id_hex]
        else:
            # Return language id hexadecimal value if not found.
            return str(language_id_hex)

    @staticmethod
    def list_window_names():
        """
        List all process
        """

        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))

        win32gui.EnumWindows(winEnumHandler, None)

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

    @staticmethod
    def scroll(clicks=0, delta_x=0, delta_y=0, delay_between_ticks=0):
        # https://stackoverflow.com/a/61436447
        """
        Source: https://docs.microsoft.com/en-gb/windows/win32/api/winuser/nf-winuser-mouse_event?redirectedfrom=MSDN

        void mouse_event(
          DWORD     dwFlags,
          DWORD     dx,
          DWORD     dy,
          DWORD     dwData,
          ULONG_PTR dwExtraInfo
        );

        If dwFlags contains MOUSEEVENTF_WHEEL,
        then dwData specifies the amount of wheel movement.
        A positive value indicates that the wheel was rotated forward, away from the user;
        A negative value indicates that the wheel was rotated backward, toward the user.
        One wheel click is defined as WHEEL_DELTA, which is 120.

        :param delay_between_ticks:
        :param delta_y:
        :param delta_x:
        :param clicks:
        :return:
        """

        if clicks > 0:
            increment = win32con.WHEEL_DELTA
        else:
            increment = win32con.WHEEL_DELTA * -1

        for _ in range(abs(clicks)):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, delta_x, delta_y, increment, 0)
            time.sleep(delay_between_ticks)

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
