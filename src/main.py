import os
import shutil
import tkinter as tk
import pyautogui
import pytesseract
import cv2

from screen_capture import ScreenCapture
from text_search import TextSearch


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
    screenshot_file_name = f"{tmp_path}/screenshot.png"
    screenshot.save(screenshot_file_name)

    pre_processing_img = cv2.imread(screenshot_file_name)
    grayscale_img = cv2.cvtColor(pre_processing_img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(f"{tmp_path}/processed_img.png", grayscale_img)
    text = pytesseract.image_to_string(grayscale_img, config='--psm 6')

    search = TextSearch()
    search.text_search(text=text)

    # remove tmp directory
    # you can comment this line if
    # you want to see the images
    shutil.rmtree(tmp_path)


if __name__ == "__main__":
    main()
