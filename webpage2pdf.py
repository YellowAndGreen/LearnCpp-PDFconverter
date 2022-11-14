import time

import numpy as np
import pyautogui

from content_resolve import get_content


def single_page_download(url: str, name: str):
    print(f'{name}:{url}')
    pyautogui.keyDown("Ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("Ctrl")
    pyautogui.write(url)
    pyautogui.press("enter")
    # 这里的等待时间过长会导致后面打印时无法输入文件名
    time.sleep(2)
    pyautogui.keyDown("Ctrl")
    pyautogui.press("p")
    pyautogui.keyUp("ctrl")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(2)
    name = name.replace("?", " ").replace(":", " ").replace("/", " ").replace("\\", " ").replace("*", " ").replace("\"",
                                                                                                                   " ")
    pyautogui.write(name)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.keyDown("Ctrl")
    pyautogui.press("w")
    pyautogui.keyUp("ctrl")


def main():
    # 获取目录信息
    # dict_lesson = np.load('dict_lesson.npy', allow_pickle=True).item()
    dict_lesson = get_content()
    np.save('dict_lesson.npy', dict_lesson)

    # 打开浏览器
    pyautogui.keyDown("winleft")
    pyautogui.press("6")
    pyautogui.keyUp("winleft")
    dict_unit = dict_lesson[list(dict_lesson.keys())[0]]
    num = 0
    for key, value in dict_unit.items():
        num += 1
        if num > 5:
            single_page_download(url=value, name=key)


if __name__ == "__main__":
    main()
