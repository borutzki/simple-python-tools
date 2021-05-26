import PyPDF2 
import tkinter as tk
from tkinter import filedialog

def get_pages(pdf_path):
    pdf_file = PyPDF2.PdfFileReader(pdf_path)
    print(pdf_file.documentInfo)
    
    pages = []
    for i in range(0,pdf_file.numPages):
        page = pdf_file.getPage(i)
        pages.append(page)
    return pages

def make_files(pages,output_directory):
    
    for i in range(0,len(pages)):

        pdf_creator = PyPDF2.PdfFileWriter()
        pdf_creator.addPage(pages[i])
        pdf_output = open(output_directory,"wb")
        pdf_creator.write(pdf_output)

def get_file_paths():
    
    root = tk.Tk()
    root.withdraw()
    
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF File","*.pdf")])

    return file_paths


def get_directory():
    print("Choose output folder")
    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askdirectory()
    return directory



# fp = file_paths[0].replace(".pdf",f"{1}.pdf")
# print(fp)

file_paths = get_file_paths()

if file_paths != "":
    output_directory = get_directory()
    
    for i in range(len(file_paths)):
        
        pages = get_pages(file_paths[i])
        make_files(pages,output_directory)