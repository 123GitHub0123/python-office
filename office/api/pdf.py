# -*- coding: utf-8 -*-


# popdf = popdf()


# 给pdf加水印-无参数
# @except_dec()
import popdf
from office.lib.decorator_utils.instruction_url import instruction


@instruction
def add_watermark() -> None:
    popdf.add_watermark()


# 给pdf加水印-有参数
# @except_dec()
@instruction
def add_watermark_by_parameters(pdf_file, mark_str, output_path=None, output_file_name=None) -> None:
    """
    必填参数：
    pdf_file:pdf的位置，例如：d:/code/程序员晚枫.pdf
    mark_str:需要添加的水印内容，例如：百度一下：程序员晚枫
    选填参数：
    output_file_name：指定添加了水印的文件名称，可以不指定，默认是：添加了水印的文件.pdf
    """
    popdf.add_watermark_by_parameters(pdf_file, mark_str, output_path, output_file_name)


# txt转pdf
# @except_dec()
@instruction
def txt2pdf(path: str, res_pdf='txt2pdf.pdf'):
    popdf.file2pdf(path, res_pdf)


# PDF加密
# @except_dec()
@instruction
def encrypt4pdf(path, password, output_path=None):
    popdf.encrypt4pdf(path, password, output_path)


# PDF解密
# @except_dec()
@instruction
def decrypt4pdf(path, password, res_pdf='decrypt.pdf'):
    popdf.decrypt4pdf(path, password, res_pdf)


# 合并pdf
# @except_dec()
@instruction
def merge2pdf(one_by_one, output):
    popdf.merge2pdf(one_by_one, output)


# todo：输入文件路径
# @except_dec()
@instruction
def pdf2docx(file_path, output_path='.'):
    popdf.pdf2docx(file_path, output_path)


# @except_dec()
@instruction
def pdf2imgs(pdf_path, out_dir):
    popdf.pdf2imgs(pdf_path, out_dir)


# @except_dec()
@instruction
def add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out):
    popdf.add_img_water(pdf_file_in, pdf_file_mark, pdf_file_out)
