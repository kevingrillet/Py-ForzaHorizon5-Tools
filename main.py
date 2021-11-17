from utils.autogpsdestination import AutoGPSDestination
from utils.autowheelspins import AutoWheelspins
from utils.handlercv2 import HandlerCv2

if __name__ == '__main__':
    cv2 = HandlerCv2()
    # cv2.show_debug_image = True
    print("Py-ForzaHorizon5-Tools")
    print("1 - AutoWheelspins")
    print("2 - AutoGPSDestination")
    print("0 - Debug")
    print("Your choice:")
    intinput = int(input())
    if intinput == 1:
        AutoWheelspins(cv2).run()
    elif intinput == 2:
        AutoGPSDestination(cv2).run()
    else:
        cv2.hwin32.list_window_names()
        cv2.dev()
