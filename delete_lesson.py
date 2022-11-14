import os

import numpy as np


def delete_lesson(delete_lesson_index, dict_lesson):
    for i in delete_lesson_index:
        dict_unit = dict_lesson[list(dict_lesson.keys())[i]]
        # 转换url地址到文件下载路径
        for name in list(dict_unit.keys()):
            filename = name.replace("?", " ").replace(":", " ").replace("/", " ").replace("\\", " ").replace("*", " ") \
                .replace("\"", "").replace("<", "")
            filename = os.path.join(download_path, filename + '.pdf')
            if os.path.exists(filename):
                os.remove(filename)


def check_lesson(dict_lesson):
    """检查所有章节中小节的完整性，返回不完整的章节索引"""
    delete_list = []
    for i in range(len(list(dict_lesson))):
        dict_unit = dict_lesson[list(dict_lesson.keys())[i]]
        # 转换url地址到文件下载路径
        for name in list(dict_unit.keys()):
            filename = name.replace("?", " ").replace(":", " ").replace("/", " ").replace("\\", " ").replace("*", " ") \
                .replace("\"", "").replace("<", "")
            # strip去除头尾的空格以防止匹配不上
            filename = os.path.join(download_path, filename.strip() + '.pdf')
            if not os.path.exists(filename):
                delete_list.append(i)
                print(filename)
                break
    return delete_list


if __name__ == '__main__':
    download_path = "E:\\temp"
    # 获取目录信息
    dict_lesson = np.load('dict_lesson.npy', allow_pickle=True).item()
    delete_list = check_lesson(dict_lesson)
    print(delete_list)
    # delete_lesson(delete_list, dict_lesson=dict_lesson)
