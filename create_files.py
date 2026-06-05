from openpyxl import Workbook
from fpdf import FPDF


# Create a CSV file with headers and one row of data
# with open("resources/data.csv", "w") as file:
#     file.write("name,age,city\n")
#     file.write("John,30,New York\n")


# Create an XLSX file with headers and one row of data
# wb = Workbook()  # create a workbook
# ws = wb.active   # get the active sheet
# ws.append(["name", "age", "city"])  # add a header row
# ws.append(["John", "30", "New York"])  # add a data row
# wb.save("resources/data.xlsx")  # save the file


# Create a PDF file with a single line of text
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Helvetica", size=12)
# pdf.cell(text="Hello from PDF")
# pdf.output("resources/data.pdf")
