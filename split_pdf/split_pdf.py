import PyPDF2
import tkinter as tk
from tkinter import filedialog
import ntpath


def get_pages(pdf_path):
    """
    Function obtaining pages as an objects and returning them as an array.
    """
    pdf_file = PyPDF2.PdfFileReader(pdf_path)
    pages = [pdf_file.getPage(i) for i in range(0, pdf_file.numPages)]

    return pages


def make_files(pages, file_name, output_directory):
    """
    Function that takes PyPDF2 pages objects and exports them as PDF files.
    """
    for i in range(0, len(pages)):
        output_path = output_directory + "/" + file_name + f"_{i+1}" + ".pdf"

        pdf_creator = PyPDF2.PdfFileWriter()
        pdf_creator.addPage(pages[i])

        pdf_output = open(output_path, "wb")
        pdf_creator.write(pdf_output)
        pdf_output.close()


def get_file_paths():
    """
    Function which obtains paths of files from user input.
    """
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF File", "*.pdf")])
    return file_paths


def get_directory():
    """
    Function which obtains output folder path from user input.
    """
    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askdirectory()
    return directory


"""
Here starts the script
"""

print("Select files to split")
file_paths = get_file_paths()
print("Choose output folder")
output_directory = get_directory()

if file_paths != "" or output_directory != "":

    for i in range(len(file_paths)):
        file_name = ntpath.basename(file_paths[i]).replace(".pdf", "")
        pages = get_pages(file_paths[i])
        make_files(pages, file_name, output_directory)

else:
    print("No files or output path selected!")
