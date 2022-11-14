import requests
from bs4 import BeautifulSoup


def get_content() -> dict:
    print("开始获取目录！")
    html = requests.get("https://www.learncpp.com/").text
    soup = BeautifulSoup(html)
    # 获取每个章节的html代码块
    lessontables = soup.findAll(name='div', attrs={"class": "lessontable"})
    dict_lesson = {}
    for lessontable in lessontables:
        # 找到当前章节的名字
        lessontable_name = lessontable.find(attrs={"class": "lessontable-header-title"}).text
        # 遍历该章内的每一小节，获取小节的名称和url
        dict_unit = {}
        for unit in lessontable.findAll(attrs={"class": "lessontable-row-title"}):
            dict_unit[unit.a.text] = unit.a.get('href')
        dict_lesson[lessontable_name] = dict_unit
    print("目录获取完成！")
    return dict_lesson
