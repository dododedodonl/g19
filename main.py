from logitech.g19 import G19

import time

if __name__ == '__main__':
    lg19 = G19(True)
    lg19.start_event_handling()
    try:
        lg19.fill_display_with_color(0,0,0)
        lg19.set_display_brightness(0)
    finally:
        lg19.stop_event_handling()
