import os
import shutil
import tkinter as tk
import pyautogui
from screen_capture import ScreenCapture


def main():
    root = tk.Tk()
    screen_capture = ScreenCapture(root=root)
    root.mainloop()

    if not screen_capture.get_capture_area_set():
        return

    tmp_path = "tmp"
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)

    screenshot = pyautogui.screenshot(
        region=screen_capture.get_captured_area())
    screenshot.save(f"{tmp_path}/screenshot.png")

    shutil.rmtree(tmp_path)


if __name__ == "__main__":
    main()
