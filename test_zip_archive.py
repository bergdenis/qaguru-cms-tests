import zipfile

import openpyxl
import pdfplumber
import io


def test_zip_archive():
    with zipfile.ZipFile("resources/archive.zip", 'w') as zip_file:
        zip_file.write("resources/data.csv")
        zip_file.write("resources/data.pdf")
        zip_file.write("resources/data.xlsx")


def test_read_csv_without_unzip():
    with zipfile.ZipFile("resources/archive.zip", 'r') as zip_file:
        with zip_file.open("resources/data.csv") as file:
            content = file.read()
            assert "John" in content.decode('utf-8')


def test_read_pdf_without_unzip():
    with zipfile.ZipFile("resources/archive.zip", 'r') as zip_file:
        with zip_file.open("resources/data.pdf") as file:
            with pdfplumber.open(io.BytesIO(file.read())) as pdf:
                text = pdf.pages[0].extract_text()
                assert "Hello from PDF" in text


def test_read_xlsx_without_unzip():
    with zipfile.ZipFile("resources/archive.zip", 'r') as zip_file:
        with zip_file.open("resources/data.xlsx") as file:
            wb = openpyxl.load_workbook(io.BytesIO(file.read()))
            assert wb.active.cell(row=1, column=1).value == "name"
