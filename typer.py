import pyautogui
import keyboard
import time


def type_code(code):
    print("\nCode is ready.")
    print("1. Click inside the editor where you want the code.")
    print("2. Press F9 to start typing.")
    print("Press ESC anytime to cancel.")

    while True:
        if keyboard.is_pressed("f9"):
            time.sleep(0.3)  # prevent accidental double trigger
            break

        if keyboard.is_pressed("esc"):
            print("Typing cancelled.")
            return

        time.sleep(0.05)

    print("Typing code...")

    for char in code:

        if keyboard.is_pressed("esc"):
            print("\nTyping stopped!")
            return

        pyautogui.write(char)

    print("\nCode typed successfully!")