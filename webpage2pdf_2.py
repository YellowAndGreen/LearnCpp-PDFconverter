import json
import time
import pyautogui
import numpy as np

from content_resolve import get_content


def open_single_page(url: str):
    pyautogui.keyDown("Ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("Ctrl")
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(2)
    # 使其直接跳到底部从而加载内容
    pyautogui.press("end")


def single_page_download(name: str, last=False):
    pyautogui.keyDown("Ctrl")
    pyautogui.press("p")
    pyautogui.keyUp("ctrl")
    time.sleep(5)
    pyautogui.press("enter")
    name = name.replace("?", " ").replace(":", " ").replace("/", " ").replace("\\", " ").replace("*", " ") \
        .replace("\"", "").replace("<", "")
    time.sleep(10)
    pyautogui.write(name)
    pyautogui.press("enter")
    if last:
        time.sleep(60)
    else:
        time.sleep(6)
    pyautogui.keyDown("Ctrl")
    pyautogui.press("w")
    pyautogui.keyUp("ctrl")


def main():
    # 获取目录信息
    dict_lesson = np.load('dict_lesson.npy', allow_pickle=True).item()
    # dict_lesson = get_content()
    # np.save('dict_lesson.npy', dict_lesson)
    # 打开浏览器
    pyautogui.keyDown("winleft")
    pyautogui.press("1")
    pyautogui.keyUp("winleft")
    # dict_unit = dict_lesson[list(dict_lesson.keys())[1]]
    # for i in range(len(list(dict_lesson.keys()))):
    for i in [14]:
        dict_unit = dict_lesson[list(dict_lesson.keys())[i]]
        # 依次序打开网页
        for value in dict_unit.values():
            open_single_page(url=value)
            time.sleep(0.5)
        time.sleep(5)
        # 依次序下载
        for index, name in enumerate(list(dict_unit.keys())[::-1]):
            if index == 0:
                # single_page_download(name, True)
                pyautogui.keyDown("Ctrl")
                pyautogui.press("w")
                pyautogui.keyUp("ctrl")
            else:
                single_page_download(name)


if __name__ == "__main__":
    main()
