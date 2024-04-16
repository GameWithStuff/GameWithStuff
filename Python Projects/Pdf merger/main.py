import os
from PyPDF2 import PdfMerger

# print(pypdf)
print("Welcome to PyDF merger!")
print("Please keep all the PDFs in a folder.")
directory = input(
    "Please enter an existing directory in which all the PDFs are as an absolute path:\n"
)
while not os.path.exists(directory):
    directory = input(
        "Please enter an existing directory in which all the PDFs are as an absolute path:\n"
    )
PDFs = []
# for i in range(numOfPdfs):
#     pdf = input(
#         "Please enter an existing directory in which all the PDFs are as an absolute path:\n"
#     )
#     while not os.path.exists(pdf):
#         directory = input("Please enter an existing directory in which all the PDFs are as an absolute path:\n")
#     PDFs.append(pdf)
pdf = "grg"
print(
    "Please enter the name of the PDFs you want merged in the order you want them merged without the file extensions and leave the input blank to proceed."
)
while pdf != '.pdf':
    pdf = input().strip() + '.pdf'
    if os.path.exists(os.path.join(directory, pdf)):
        PDFs.append(os.path.join(directory, pdf))
        # print("HI")
newName = input("Enter the new name of the merged PDF without file extension:\n") + ".pdf"
merger = PdfMerger()
for pdf in PDFs:
    try:
        merger.append(pdf)
    except:
        print("An error occured while merging", pdf)
merger.write(newName)
print('Merged Successfully!!')
while True:
    pass