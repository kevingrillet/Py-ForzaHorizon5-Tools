from utils.autogpsdestination import AutoGPSDestination
from utils.autowheelspins import AutoWheelspins
from utils.handlercv2 import HandlerCv2

if __name__ == '__main__':
    hcv2 = HandlerCv2()
    # hcv2.show_debug_image = True
    print("Py-ForzaHorizon5-Tools")
    print("1 - AutoWheelspins")
    print("2 - AutoGPSDestination")
    print("0 - Dev")
    print("Your choice:")
    intinput = int(input())
    if intinput == 1:
        AutoWheelspins(hcv2).run()
    elif intinput == 2:
        AutoGPSDestination(hcv2).run()
    else:
        hcv2.hwin32.list_window_names()
        hcv2.dev()
