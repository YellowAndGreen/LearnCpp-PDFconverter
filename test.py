import json
import time
import pyautogui
import numpy as np

from content_resolve import get_content


def single_page_download(url: str, name: str):
    print(f'{name}:{url}')
    pyautogui.keyDown("Ctrl")
    pyautogui.press("t")
    pyautogui.keyUp("Ctrl")
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.keyDown("Ctrl")
    pyautogui.press("p")
    pyautogui.keyUp("ctrl")
    time.sleep(4)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write('name')
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.keyDown("Ctrl")
    pyautogui.press("w")
    pyautogui.keyUp("ctrl")


def main():
    # 获取目录信息
    # dict_lesson = np.load('dict_lesson.npy', allow_pickle=True).item()
    # # dict_lesson = get_content()
    # # np.save('dict_lesson.npy', dict_lesson)
    #
    # # 打开浏览器
    pyautogui.keyDown("winleft")
    pyautogui.press("1")
    pyautogui.keyUp("winleft")
    pyautogui.press("end")
    # dict_unit = dict_lesson[list(dict_lesson.keys())[0]]
    # for key, value in dict_unit.items():
    #     single_page_download(url=value, name=key)
    #     break
    # single_page_download(url='https://www.learncpp.com/cpp-tutorial/compiling-your-first-program/', name='Compiling your first program')
    # single_page_download(url='https://www.learncpp.com/cpp-tutorial/compiling-your-first-program/', name='Compiling your first program')


if __name__ == "__main__":
    main()
