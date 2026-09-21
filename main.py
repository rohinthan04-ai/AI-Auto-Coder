import pyautogui
import keyboard
import time

from gemini import solve_screen


def capture_and_solve():
    print("\nCapturing screen...")

    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")

    print("Screenshot captured!")
    print("Sending screenshot to Gemini...")

    try:
        code = solve_screen("screen.png")

        print("\n========== GEMINI CODE ==========\n")
        print(code)
        print("\n=================================\n")

    except Exception as e:
        print("\nGemini error:")
        print(e)


print("AI AutoCoder started.")
print("Press F8 to capture screen and solve.")
print("Press ESC to exit.")

while True:

    if keyboard.is_pressed("f8"):
        capture_and_solve()
        time.sleep(1)

    if keyboard.is_pressed("esc"):
        print("Exiting...")
        break

    time.sleep(0.05)