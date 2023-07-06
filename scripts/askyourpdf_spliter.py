# 因为askyourpdf只能上传不超过300页，这里进行分页
# pip install pypdf
# https://github.com/py-pdf/pypdf
import sys
from pypdf import PdfReader, PdfWriter


def split_pdf(input_path, max_pages, output_dir):
    pdf_name = input_path.split('/')[-1].replace('.pdf', '')
    with open(input_path, 'rb') as file:
        pdf = PdfReader(file)
        total_pages = len(pdf.pages)

        # 计算需要分割成多少本书
        num_books = (total_pages + max_pages - 1) // max_pages

        for book_number in range(num_books):
            output = PdfWriter()

            # 计算每本书的起始和结束页数
            start_page = book_number * max_pages
            end_page = min((book_number + 1) * max_pages, total_pages)

            # 将页范围内的页面添加到输出文件
            for page in range(start_page, end_page):
                output.add_page(pdf.pages[page])

            # 生成输出文件名
            output_path = f"{output_dir}/{pdf_name}_{book_number + 1}.pdf"

            # 将输出写入新的PDF文件
            with open(output_path, 'wb') as output_file:
                output.write(output_file)

            print(f"生成文件: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("请传入pdf文件路径...")
    max_pages_per_book = 300
    output_dir = "/Users/kuanhsiaokuo/Migrations/pdfs/splited"
    split_pdf(sys.argv[1], max_pages_per_book, output_dir)
