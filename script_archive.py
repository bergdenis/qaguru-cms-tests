from zipfile import ZipFile

with ZipFile("tmp/sample-1.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read("sample-1/")
    print(text)
    zip_file.extract("sample-1/", path="tmp")