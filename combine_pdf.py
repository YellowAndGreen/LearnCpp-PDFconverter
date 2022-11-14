import os

import fitz

# doc = fitz.open('C:\\Users\\Administrator\\Desktop\\LeetCode+101.pdf')
# doc2 = fitz.open('C:\\Users\\Administrator\\Desktop\\雷达上采样.pdf')
# page_count = doc.page_count
# doc.insert_pdf(doc2)
# toc = doc.get_toc()
# toc.append([1, 'test', page_count + 1])
# doc.set_toc(toc)
# doc.save("C:\\Users\\Administrator\\Desktop\\test.pdf")
import numpy as np


def insert_lesson(doc: fitz.fitz.Document, chapter: int, chapter_name: str, lesson: dict):
    """
    :param doc: pdf object
    :param chapter_name:
    :param chapter: chapter number
    :param lesson: {name:pdf_path}
    :return:
    """
    # 初始化文档以便之后添加内容
    toc = doc.get_toc()
    toc.append([1, "Chapter " + str(chapter) + ' ' + chapter_name, doc.page_count + 1])  # 插入当前章节书签
    count = 1
    for name, pdf_path in lesson.items():
        temp_doc = fitz.open(pdf_path)
        page_count = doc.page_count  # 保存当前页数以便之后加入书签
        doc.insert_pdf(temp_doc)
        toc.append([2, str(count) + '. ' + name, page_count + 1])
        count += 1
    doc.set_toc(toc)
    return doc


if __name__ == "__main__":
    download_path = "E:\\temp"
    # 获取目录信息
    dict_lesson = np.load('dict_lesson.npy', allow_pickle=True).item()
    # 创建一个新的文档
    doc = fitz.open()
    total_num = len(list(dict_lesson))
    for i in range(len(list(dict_lesson))):
        print(f'{i+1}/{total_num}')
        dict_unit = dict_lesson[list(dict_lesson.keys())[i]]
        # 转换url地址到文件下载路径
        for name in list(dict_unit.keys()):
            filename = name.replace("?", " ").replace(":", " ").replace("/", " ").replace("\\", " ").replace("*", " ") \
                .replace("\"", "").replace("<", "")
            dict_unit[name] = os.path.join(download_path, filename.strip() + '.pdf')
        doc = insert_lesson(doc, i, list(dict_lesson.keys())[i], dict_unit)

    doc.save("E:\\temp\\out\\out.pdf")
