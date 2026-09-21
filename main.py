import pyautogui
import keyboard
import time

def capture_screen():
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    print("Screenshot captured!")

print("AI AutoCoder started.")
print("Press F8 to capture the screen.")
print("Press ESC to exit.")

while True:

    if keyboard.is_pressed("f8"):
        capture_screen()
        time.sleep(1)

    if keyboard.is_pressed("esc"):
        print("Exiting...")
        break

    time.sleep(0.05)