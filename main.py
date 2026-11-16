
import pyautogui
import pyperclip
import keyboard
import threading

from gemini import solve_screen


processing_lock = threading.Lock()


def capture_and_type():

    # Prevent multiple F8 triggers while processing
    if not processing_lock.acquire(blocking=False):
        print("Already processing. Please wait...")
        return

    try:
        print("\nCapturing screen...")

        screenshot = pyautogui.screenshot()
        screenshot.save("screen.png")

        print("Screenshot captured!")
        print("Analyzing with Gemini...")

        code = solve_screen("screen.png")

        if not code or not code.strip():
            print("No code was generated.")
            return

        print("\n========== GENERATED CODE ==========\n")
        print(code)
        print("\n====================================\n")

        print("Pasting code into editor...")

        pyperclip.copy(code)
        pyautogui.hotkey("ctrl", "v")

        print("Code inserted successfully!")

    except Exception as e:
        print(f"\nError: {e}")

    finally:
        processing_lock.release()


print("================================")
print("          AI AutoCoder")
print("================================")
print("F8  = Analyze screen + Generate + Paste")
print("ESC = Exit")
print()
print("Keep your code editor focused.")
print("Waiting for hotkey...")

keyboard.add_hotkey(
    "f8",
    capture_and_type,
    suppress=True,
    trigger_on_release=True
)

try:
    keyboard.wait("esc")
finally:
    keyboard.unhook_all_hotkeys()
    print("\nAI AutoCoder stopped.")
