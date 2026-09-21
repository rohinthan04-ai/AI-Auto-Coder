import pyautogui
import keyboard
import time

from gemini import solve_screen
from typer import type_code


latest_code = None


def capture_and_solve():
    global latest_code

    print("\nCapturing screen...")

    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")

    print("Screenshot captured!")
    print("Sending screenshot to Gemini...")

    try:
        latest_code = solve_screen("screen.png")

        print("\n========== GEMINI CODE ==========\n")
        print(latest_code)
        print("\n=================================\n")

        print("Code is ready.")
        print("Click inside the coding editor.")
        print("Press F9 to type the code.")
        print("Press ESC to cancel.")

    except Exception as e:
        print("\nGemini error:")
        print(e)
        latest_code = None


print("================================")
print("       AI AutoCoder")
print("================================")
print("F8 = Capture + Solve")
print("F9 = Type generated code")
print("ESC = Stop")
print()

while True:

    if keyboard.is_pressed("f8"):
        capture_and_solve()
        time.sleep(1)

    if keyboard.is_pressed("f9") and latest_code:
        type_code(latest_code)
        time.sleep(1)

    if keyboard.is_pressed("esc"):
        print("Exiting...")
        break

    time.sleep(0.05)