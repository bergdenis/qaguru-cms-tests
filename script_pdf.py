import os

from pypdf import PdfReader

reader = PdfReader("tmp/pytest_book.pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

assert "Simple, Rapid, Effective, and Scalable" in reader.pages[1]
print(os.path.getsize("tmp/pytest_book.pdf"))
assert os.path.getsize("tmp/pytest_book.pdf") == 3081510

