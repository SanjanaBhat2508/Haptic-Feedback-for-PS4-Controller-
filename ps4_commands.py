import evdev
import pygame

# Find the PS4 controller device
def find_controller():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for device in devices:
        if "Wireless Controller" in device.name or "DualShock 4" in device.name:
            return device
    return None

# Initialize pygame for haptic feedback
pygame.init()
pygame.joystick.init()

# Initialize the joystick for haptic feedback
def init_joystick():
    joystick = None
    if pygame.joystick.get_count() > 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    return joystick

# Read events from the controller
def detect_l3_btn(controller):
    try:
        for event in controller.read_loop():
            if event.type == evdev.ecodes.EV_KEY:  # Button press/release
                key_event = evdev.categorize(event)
                if "BTN_THUMBL" in key_event.keycode:  # L3 button
                    print(f"Button {key_event.keycode} {'pressed' if event.value else 'released'}")
                    return event.value == 1  # True if pressed
    except:
        pass
    return False
