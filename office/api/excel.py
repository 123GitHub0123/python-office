#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: excel.py
# Mail: 1957875073@qq.com
# Created Time:  2022-4-25 10:17:34
# Description: 有关 excel 的自动化操作
#############################################
# from office.core.ExcelType import MainExcel
# mainExcel = MainExcel()

import poexcel
from win32com.client import DispatchEx

# todo:输出文件路径
# @except_dec()
from office.lib.decorator_utils.instruction_url import instruction


@instruction
def fake2excel(columns=['name'], rows=1, path='./fake2excel.xlsx', language='zh_CN'):
    poexcel.fake2excel(columns, rows, path, language)


# 多个excel，合并到一个excel的不同sheet中
# @except_dec()
@instruction
def merge2excel(dir_path, output_file='merge2excel.xlsx'):
    """
    :param dir_path:
    :param output_file:
    :return:
    """
    poexcel.merge2excel(dir_path, output_file)


# 同一个excel里的不同sheet，拆分为不同的excel文件
# @except_dec()
@instruction
def sheet2excel(file_path, output_path='./'):
    poexcel.sheet2excel(file_path, output_path)


# @except_dec()
@instruction
def merge2sheet(dir_path, output_sheet_name: str = 'Sheet1', output_excel_name: str = 'merge2sheet'):
    poexcel.merge2sheet(dir_path, output_sheet_name, output_excel_name)


# 搜索excel中指定内容的文件、行数、内容详情
# PR内容 & 作者：https://gitee.com/CoderWanFeng/python-office/pulls/10
# @except_dec()
@instruction
def find_excel_data(search_key: str, target_dir: str):
    poexcel.find_excel_data(search_key, target_dir)


# 按指定列的内容，拆分excel
# PR内容 & 作者：：https://gitee.com/CoderWanFeng/python-office/pulls/11
# @except_dec()
@instruction
def split_excel_by_column(filepath: str, column: int, worksheet_name: str = None):
    poexcel.split_excel_by_column(filepath, column, worksheet_name)


@instruction
def excel2pdf(excel_path, pdf_path):
    """
    https://blog.csdn.net/qq_57187936/article/details/125605967
    """
    poexcel.excel2pdf(excel_path, pdf_path)
