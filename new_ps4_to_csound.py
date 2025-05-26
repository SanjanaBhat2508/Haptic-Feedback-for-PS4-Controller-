import os
import time
import pygame
import threading
from ps4_commands import find_controller, detect_l3_btn, init_joystick

# Global variable to synchronize actions (True means start)
start_feedback = False

# Initialize pygame for haptic feedback
pygame.init()
pygame.joystick.init()

# Find and initialize the PS4 controller
controller = find_controller()
if controller is None:
    print("No PS4 controller found!")
    exit()

# Initialize the joystick for haptic feedback
joystick = init_joystick()
if joystick is None:
    print("No joystick found!")
    exit()

# Function to provide haptic feedback (vibration)
def give_haptic_feedback():
    global start_feedback
    while not start_feedback:
        time.sleep(0.01)  # Wait until the signal to start
    # Rumble the controller (high-frequency, low-frequency, duration)
    joystick.rumble(1.0, 1.0, 1000)  # Adjust the values for different intensity and duration
    time.sleep(1)  # Wait for rumble to finish
    joystick.stop_rumble()  # Stop the rumble after the specified duration

# Function to play sound using Csound
def play_sound():
    global start_feedback
    while not start_feedback:
        time.sleep(0.01)  # Wait until the signal to start
    os.system("csound /home/sanjana/Documents/Csound_try/voice_notification.csd")  # Play sound
    print("Playing sound...")

# Main loop to detect the L3 button press
while True:
    if detect_l3_btn(controller):  # Check if L3 button is pressed
        print("L3 button pressed!")

        start_feedback = False

        # Start playing sound and give haptic feedback concurrently
        sound_thread = threading.Thread(target=play_sound)
        haptic_thread = threading.Thread(target=give_haptic_feedback)

        sound_thread.start()
        haptic_thread.start()

        # Set the flag to True to allow the threads to begin executing their actions
        start_feedback = True

        sound_thread.join()
        haptic_thread.join()

        print("Haptic feedback triggered!")
        time.sleep(2)  # Wait for 2 seconds before checking again
        print("Can try again")
