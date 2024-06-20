from tkinter import *
from tkinter import filedialog
import os
from PyPDF2 import PdfMerger  # Import PyPDF2 library for merging PDFs


def browse_directory(selected_dir, entry_dir, list_box,list_box_merged):
    
    selected_dir=filedialog.askdirectory(title='Select a directory')
    if selected_dir:
        entry_dir.delete(0,END)
        entry_dir.insert(0,selected_dir)
        update_list_box(selected_dir,list_box)
        merged_pdf(selected_dir,list_box_merged)

def update_list_box(selected_dir,list_box):
    if not selected_dir:
        return
    pdf_files=[]
    for file in os.listdir(selected_dir):
        if file.endswith(".pdf"):
            pdf_files.append(file)
    list_box.delete(0,END)
    for i in pdf_files:
        list_box.insert(END,i)
    

def merged_pdf(selected_dir,list_box_merged):
    if not selected_dir:
        return  # Do nothing if no directory is selected

    pdf_merger = PdfMerger()
    for filename in os.listdir(selected_dir):
        if filename.endswith(".pdf"):
            filepath = os.path.join(selected_dir, filename)
            pdf_merger.append(filepath)
    merged_filename='merged.pdf'
    with open(merged_filename,'wb') as outputfile:
        pdf_merger.write(outputfile)
    
    list_box_merged.insert(END,f"Merged File Name: {merged_filename}")
    list_box_merged.insert(END,f"Saved in: {os.getcwd()}")