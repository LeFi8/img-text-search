import pyautogui
import os, shutil

tmp_path = "tmp"

if not os.path.exists(tmp_path):
    os.mkdir(tmp_path)

screenshot = pyautogui.screenshot(f"{tmp_path}/screenshot.png")
shutil.rmtree(tmp_path)